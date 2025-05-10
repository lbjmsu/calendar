drop table 834_group5_user;
drop table 834_group5_event;

create table 834_group5_user (
    uid int primary key,
    accountType varchar(50),
    username varchar(50),
    password varchar(50)
);

create table 834_group5_event (
    eventID int primary key,
    eventCreatorID int,
    eventType varchar(50),
    eventDate varchar(25),
    eventTime varchar(50),
    eventLength double,
    eventName varchar(255),
    eventDescription varchar(255),
    constraint ecID foreign key (eventCreatorID) references 834_group5_user(uid) on delete cascade
);

-- Insert fake users
insert into 834_group5_user (uid, accountType, username, password) values
(1, 'manager', 'admin_john', 'securepass123'),
(2, 'manager', 'user_jane', 'pass456'),
(3, 'user', 'michael99', 'mikepass789'),
(4, 'user', 'mod_emily', 'modpass321');

-- Insert fake events
insert into 834_group5_event (eventID, eventCreatorID, eventType, eventDate, eventTime, eventLength, eventName, eventDescription) values
(101, 1, 'Meeting', '2025-05-15', '10:00 AM', 1.5, 'Weekly Admin Sync', 'Discussion of weekly administrative matters'),
(102, 2, 'Workshop', '2025-06-01', '02:00 PM', 2.0, 'JavaScript Basics', 'Introductory workshop for JavaScript beginners'),
(103, 3, 'Webinar', '2025-05-20', '06:00 PM', 1.0, 'AI Trends 2025', 'A look at the upcoming trends in Artificial Intelligence'),
(104, 4, 'Training', '2025-05-25', '09:00 AM', 3.0, 'Moderation Tools Training', 'Training session for new moderators');

ALTER TABLE 834_group5_event ADD COLUMN eventDate DATE;

UPDATE 834_group5_event
SET eventDate = DATE_FORMAT(STR_TO_DATE(eventDate, '%Y-%m-%d'), '%m/%d/%Y');

ALTER TABLE 834_group5_event DROP COLUMN eventDate;

ALTER TABLE 834_group5_event CHANGE eventDate_temp eventDate DATE;

UPDATE 834_group5_event
SET eventDate = DATE_FORMAT(STR_TO_DATE(eventDate, '%Y-%m-%d'), '%m/%d/%Y');