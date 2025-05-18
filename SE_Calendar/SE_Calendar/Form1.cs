using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Diagnostics.Eventing;
using System.Drawing;
using System.Globalization;
using System.Linq;
using System.Management.Instrumentation;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml.Linq;
using MySql.Data.MySqlClient;
using Mysqlx.Crud;

namespace SE_Calendar
{
    public partial class Form1 : Form
    {
        List<Event> events = new List<Event>();
        private List<Attendee> attendeesList = new List<Attendee>();
        private int uID;
        private string accountType;
        private DateTime? selectedEventDate = null;

        public Form1()
        {
            InitializeComponent();
        }

        //  LOGIN PANEL
        //  Event Handler: Login Button Button (Login Panel)
        private void button1_Click(object sender, EventArgs e)
        {
            //  Check if contents of textbox1 (username) and textbox2 (password) exist in the database
            string username = textBox1.Text;
            string password = textBox2.Text;

            //  Create connection to database
            string connStr = "server=csitmariadb.eku.edu;user=student;database=csc340_db;port=3306;password=Maroon@21?;";
            MySqlConnection conn = new MySqlConnection(connStr);

            //  Create query to return any record with the provided username
            string commandStrUsernameSelect = "SELECT * FROM 834_group5_user WHERE username = @user";
            MySqlCommand command = new MySqlCommand(commandStrUsernameSelect, conn);
            command.Parameters.AddWithValue("@user", username);

            //  Open connection and attempt to read requested record
            conn.Open();
            MySqlDataReader reader = command.ExecuteReader();

            //  Correct Username
            if(reader.Read())
            {
                //  Successful login
                if (reader.GetString(3) == password)
                {
                    //  Store current user information
                    uID = reader.GetInt32(0);
                    accountType = reader.GetString(1);

                    //  If account is a manager, show the "Schedule events" button.
                    if(accountType == "manager")
                    {
                        button17.Visible = true;
                    }

                    //  Clear "Login" textboxes
                    textBox1.Text = string.Empty;
                    textBox2.Text = string.Empty;

                    //  Load events to monthly event list
                    RetrieveListOfEvents();
                    LoadEventList();

                    //  GOTO: login screen
                    panelLogin.Visible = false;
                    splitContainer2.Visible = true;
                }
                //  Incorrect password
                else
                {
                    //  GOTO: password error screen
                    panelLogin.Visible = false;
                    panelInvalidPassword.Visible = true;
                }
            }
            //  Incorrect username
            else
            {
                //  GOTO: username error screen
                panelLogin.Visible = false;
                panelInvalidUsername.Visible = true;
            }

            //  Close connection to database
            conn.Close();
        }

        //  Event Handler: Create Account Button (Login Panel)
        private void button2_Click(object sender, EventArgs e)
        {
            panelLogin.Visible = false;
            panelCreateAccount.Visible = true;
        }

        //  Event Handler: Return to Login Screen (Independent of Panel).
        private void ReturnToLoginEvent(object sender, EventArgs e)
        {
            //  Get parent panel for the calling button
            Control s = sender as Control;
            Control panel = s.Parent.Parent;

            //  Reset login textboxes
            textBox1.Text = string.Empty;
            textBox2.Text = string.Empty;

            //  Return to Login Screen
            panel.Visible = false;
            panelLogin.Visible = true;
        }



        //  CREATE ACCOUNT PANEL
        //  Event Handler: Create Account Button (Create Account Panel)
        private void button8_Click(object sender, EventArgs e)
        {
            string username = textBox3.Text;
            string password = textBox4.Text;
            string passwordConfirmation = textBox5.Text;


            //  Create connection to database
            string connStr = "server=csitmariadb.eku.edu;user=student;database=csc340_db;port=3306;password=Maroon@21?;";
            MySqlConnection conn = new MySqlConnection(connStr);

            //  Create command to check if user-supplied username exists in database already
            string commandStrCheckExistsUsername = "SELECT username FROM 834_group5_user WHERE username = @user";
            MySqlCommand commandCheckExistsUsername = new MySqlCommand(commandStrCheckExistsUsername, conn);
            commandCheckExistsUsername.Parameters.AddWithValue("@user", username);

            //  Open connection to database and execute username check query
            conn.Open();
            MySqlDataReader reader = commandCheckExistsUsername.ExecuteReader();

            //  ERROR: Username is empty
            if(username == string.Empty)
            {
                //  GOTO: create account error screen
                panelCreateAccount.Visible = false;
                panelCreateErrorEmptyUsername.Visible = true;
            }

            //  ERROR: Username is in database already
            else if (reader.Read())
            {
                //  GOTO: create account error screen
                panelCreateAccount.Visible = false;
                panelCreateErrorUsernameExists.Visible = true;
            }

            //  ERROR: Password and password confirmation do not match
            else if (password != passwordConfirmation)
            {
                //  GOTO: create account error screen
                panelCreateAccount.Visible = false;
                panelCreateErrorPasswords.Visible = true;
            }

            //  Password and Password Confirmation match
            else
            {
                //  Close username check reader
                reader.Close();

                //  Create query to return most recent uID
                string commandStrMostRecentUID = "SELECT uid FROM 834_group5_user ORDER BY uid DESC";
                MySqlCommand cmdMostRecentUID = new MySqlCommand(commandStrMostRecentUID, conn);

                //  Read and store the most recent uID
                reader = cmdMostRecentUID.ExecuteReader();
                int mostRecentUID;

                //  If no records are returned...
                if (!reader.Read())
                {
                    //  There are no users in the database -- set most recent user id to 0
                    mostRecentUID = 0;
                }
                else
                {
                    //  There are users in the database -- set most recent user id to user id of first record
                    mostRecentUID = reader.GetInt32(0);
                }

                //  Close the most recent user id reader
                reader.Close();

                //  Create query to create a user account with the supplied credentials
                string commandStrCreateAccount = "INSERT INTO 834_group5_user VALUES (@uid, \'user\', @username, @password)";
                MySqlCommand commandCreateAccount = new MySqlCommand(commandStrCreateAccount, conn);
                commandCreateAccount.Parameters.AddWithValue("@uid", mostRecentUID+1);
                commandCreateAccount.Parameters.AddWithValue("@username", username);
                commandCreateAccount.Parameters.AddWithValue("@password", password);

                //  Insert account into database
                commandCreateAccount.ExecuteNonQuery();

                //  Clear "Create account" textboxes
                textBox3.Text = string.Empty;
                textBox4.Text = string.Empty;
                textBox5.Text = string.Empty;

                //  GOTO: create account success screen
                panelCreateAccount.Visible = false;
                panelCreateAccountSuccess.Visible = true;
            }

            //  Close connection to database
            conn.Close();
        }

        //  Event Handler: Return to Create Account Screen (Independent of Panel)
        private void ReturnToCreateAccountEvent(object sender, EventArgs e)
        {
            //  Get parent panel for the calling button
            Control s = sender as Control;
            Control panel = s.Parent.Parent;

            //  Reset password textboxes
            textBox4.Text = string.Empty;
            textBox5.Text = string.Empty;

            //  Return to Create Account Screen
            panel.Visible = false;
            panelCreateAccount.Visible = true;
        }



        //  MAIN MENU PANEL
        //  Event Handler: Add Event Button (Main Menu Panel)
        private void button3_Click_1(object sender, EventArgs e)
        {
            //  GOTO: Add Event Panel
            splitContainer2.Visible = false;
            panelAddEvent.Visible = true;
        }
        
        //  Event Handler: Delete Event Button (Main Menu Panel)
        private Event eventToDelete;
        private void button4_Click(object sender, EventArgs e)
        {
            //STEP 1: Check if a date was selected
            if (selectedEventDate == null)
            {
                MessageBox.Show("⚠️ Please select a date from the calendar.");
                return;
            }

            //STEP 2: Filter events for selected date
            DateTime date = selectedEventDate.Value;
            var matchedEvents = events
                .Where(ev => DateTime.TryParse(ev.eventDate, out DateTime edate) && edate.Date == date.Date)
                .ToList();

            //STEP 3: No events found
            if (matchedEvents.Count == 0)
            {
                MessageBox.Show("❌ No events found for the selected date.");
                return;
            }

            //STEP 4: Show events in checkbox list
            checkedListBox1.Items.Clear();
            foreach (var ev in matchedEvents)
            {
                string display = $"{ev.eventTime} - {ev.eventName} ({ev.eventType})";
                checkedListBox1.Items.Add(new EventItem { EventID = ev.eventID, Display = display });
            }

            // Moves from main menu to Events Associated screen
            splitContainer2.Visible = false;
            splitContainer7.Visible = true;
        }

        //  Event Handler: Edit Event Button (Main Menu Panel)
        private void button5_Click(object sender, EventArgs e)
        {
            if (selectedEventDate == null)
            {
                MessageBox.Show("Please select a date first.");
                return;
            }

            DateTime date = selectedEventDate.Value;
            var matchedEvents = events
                .Where(ev => DateTime.TryParse(ev.eventDate, out DateTime edate) && edate.Date == date.Date)
                .ToList();

            if (matchedEvents.Count == 0)
            {
                MessageBox.Show(" No events found for the selected date.");
                return;
            }

            checkedListBox6.Items.Clear();
            foreach (var ev in matchedEvents)
            {
                string display = $"{ev.eventTime} - {ev.eventName} ({ev.eventType})";
                checkedListBox6.Items.Add(new EventItem { EventID = ev.eventID, Display = display });
            }

            splitContainer2.Visible = false;
            splitContainer1.Visible = true; // go to Events Associated for Edit       

        }

        //  Event Handler: View Event Button (Main Menu Panel)
        private void button6_Click(object sender, EventArgs e)
        {
            //  If an event has been selected in the monthly event list...
            if (listBox1.SelectedItem is EventItem selectedEvent)
            {
                //  GOTO: Event View Panel
                splitContainer2.Visible = false;
                splitContainer10.Visible = true;

                //  Get event from event list using selected event's ID
                Event found = getEventById(selectedEvent.EventID);

                //  Set event view textboxes to selected event's information
                textBox15.Text = found.eventName.ToString();
                textBox16.Text = found.eventDescription.ToString();
                textBox17.Text = found.eventDate.ToString();
                textBox18.Text = found.eventTime.ToString();
                textBox19.Text = found.eventType.ToString();
            }
        }

        //  Event Handler: Schedule Event Button (Main Menu Panel)
        private void button17_Click(object sender, EventArgs e)
        {
            //  GOTO: Schedule Event Attendees Panel
            splitContainer2.Visible = false;
            splitContainer11.Visible = true;

            //  Fill attendees panel with users from database
            checkedListBox2.Items.Clear();
            retrieveListOfUsers(uID);
        }

        //  Event Handler: Date of calendar on Main Menu changed
        private void monthCalendar1_DateChanged(object sender, DateRangeEventArgs e)
        {
            //  Updates the items in the edit/delete event checkedListBox
            DateTime selectedDate = e.Start;

            selectedEventDate = selectedDate;
            checkedListBox1.Items.Clear();

            var matchedEvents = events
                .Where(ev => DateTime.TryParse(ev.eventDate, out DateTime edate) && edate.Date == selectedDate.Date)
                .ToList();

            if (matchedEvents.Count == 0)
            {
                selectedEventDate = null;  //No matching events = null
                return;
            }

            selectedEventDate = selectedDate; //Store selected date

            foreach (var ev in matchedEvents)
            {
                string display = $"{ev.eventTime} - {ev.eventName}";
                checkedListBox1.Items.Add(new EventItem { EventID = ev.eventID, Display = display });

            }
        }

        //  Add users to Schedule Event Attendees Panel
        private void retrieveListOfUsers(int uid)
        {

            try
            {

                string connStr = "server=csitmariadb.eku.edu;user=student;database=csc340_db;port=3306;password=Maroon@21?;";
                using (MySqlConnection conn = new MySqlConnection(connStr))
                {
                    conn.Open();

                    string sql = $"SELECT * FROM 834_group5_user WHERE uID != {uid};";
                    MySqlCommand cmd = new MySqlCommand(sql, conn);
                    using (MySqlDataReader reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            var attendee = new Attendee
                            {
                                Id = (int)reader["uid"],
                                Name = (string)reader["username"],
                            };

                            checkedListBox2.Items.Add(attendee);

                        }
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error loading events: " + ex.Message);
            }
        }



        //  ADD EVENT PANEL
        //  Event Handler: Add Event Button (Add Event Panel)
        private void button10_Click(object sender, EventArgs e)
        {

            //  Validate event time input
            bool invalidHour = !Int32.TryParse(textBox9.Text, out int hour) || hour < 1 || hour > 12;
            bool invalidMinute = !Int32.TryParse(textBox20.Text, out int minute) || minute < 0 || minute > 59;
            bool invalidAMPM = comboBox3.Text != "AM" && comboBox3.Text != "PM";

            //  Invalid Date Entered
            if (invalidHour || invalidMinute || invalidAMPM)
            {
                //  GOTO: invalid date screen
                panelAddEvent.Visible = false;
                panelAddEventErrorInvalidTime.Visible = true;
                return;
            }

            //  Validate event length input
            if (!float.TryParse(textBox10.Text, out _))
            {
                //  GOTO: invalid time screen
                panelAddEvent.Visible = false;
                panelAddEventErrorInvalidLength.Visible = true;
                return;
            }

            //  Parse table values from panel textboxes
            string eventName = textBox6.Text;
            string eventDescription = textBox7.Text;
            DateTime eventDate = DateTime.Parse(textBox8.Text + " 12:00:00");
            float eventLength = float.Parse(textBox10.Text);

            //  Create event time string from hour and minute textboxes, and AM/PM dropdown menu
            string eventHourStr = textBox9.Text.Length == 1 ? "0" + textBox9.Text : textBox9.Text;
            string eventMinuteStr = textBox20.Text.Length == 1 ? "0" + textBox20.Text : textBox20.Text;
            string eventTime = eventHourStr + ":" + eventMinuteStr + " " + comboBox3.Text;

            //  INTRODUCING: SIMPLIFIED EVENT TIME -- Turns an hour, minute, and am/pm value into a single float in a [0,24) range.
            //      USE: Convert event time to a float value for easy comparison of overlaps
            //
            //  SIMPLIFIED EVENT TIME =
            //      if hour != 12:  HOUR + MINUTE + AM/PM
            //      if hour == 12: (HOUR + MINUTE + AM/PM + 12) % 24
            //
            //  EVENTS using SIMPLIFIED EVENT TIME are stored as: (EVENT TIME, EVENT LENGTH), where EVENT LENGTH is a positive non-zero float.
            //
            //  An OVERLAP occurs between two events using SIMPLIFIED EVENT TIME occurs when:
            //      A.TIME < B.TIME   &&  A.TIME + A.LENGTH > B.TIME    OR
            //      B.TIME < A.TIME   &&  B.TIME + B.LENGTH > A.TIME
            //
            //
            //  EXAMPLE: Do Event A (12:30 PM, 1.5h) and Event B (1:45 PM, 2h) conflict?
            //
            //  SIMPLIFIED A: (12.5, 1.5)
            //   -> 12:30 = (12 + 0.5  + 12 + 12) % 24  = 12.5
            //
            //  SIMPLIFIED B: (13.75, 2)
            //   -> 1:45  =  1  + 0.75 + 12             = 13.75
            //
            //      Does Event B start during Event A?
            //      A.TIME < B.TIME && A.TIME + A.LENGTH > B.TIME   
            //      12.5   < 13.75                                  TRUE
            //                         12.5  +  1.5      > 13.75    TRUE
            //      --> YES, Event B starts during Event A.
            //
            //      Does Event A start during Event B?
            //      B.TIME < A.TIME && B.TIME + B.LENGTH > A.TIME       
            //      13.75  < 12.5                                   FALSE
            //                         13.75  + 2        > 12.5     TRUE
            //      --> NO,  Event A does not start during Event B.
            //
            //      Since Event B starts during Event A, there is a conflict.

            //  Prepare time string for use in deriving Simplified Event Time
            double eventHour = double.Parse(eventHourStr);
            double eventMinute = double.Parse(eventMinuteStr);
            string eventAMPM = eventTime.Substring(6, 2);

            //  Represent event time in Simplified Event Time
            double eventTimeSimplifiedHour = eventHour;
            double eventTimeSimplifiedMinute = eventMinute / 60;
            double eventTimeSimplifiedAMPM = eventAMPM == "AM" ? 0 : 12;
            if (eventHour == 12)
            {
                eventTimeSimplifiedAMPM += 12;
                eventTimeSimplifiedAMPM %= 24;
            }
            double eventTimeSimplified = eventTimeSimplifiedHour + eventTimeSimplifiedMinute + eventTimeSimplifiedAMPM;


            //  Create connection to database
            string connStr = "server=csitmariadb.eku.edu;user=student;database=csc340_db;port=3306;password=Maroon@21?;";
            MySqlConnection conn = new MySqlConnection(connStr);

            //  Create command to retrieve all events on the same day as the user event
            string commandStrGetEventsByDay = "SELECT * FROM 834_group5_event WHERE eventDate = @date";
            MySqlCommand commandGetEventsByDay = new MySqlCommand(commandStrGetEventsByDay, conn);
            commandGetEventsByDay.Parameters.AddWithValue("@date", eventDate.ToString("yyyy-MM-dd"));

            //  Read events that occur on the same day as the new event
            conn.Open();
            MySqlDataReader reader = commandGetEventsByDay.ExecuteReader();

            while (reader.Read())
            {
                //  Get Event time and length from record
                string dbEventTime = reader.GetString(3);
                float dbEventLength = reader.GetFloat(4);

                //  Convert database event time to a float value for easy comparison
                double dbEventHour = double.Parse(dbEventTime.Substring(0, 2));
                double dbEventMinute = double.Parse(dbEventTime.Substring(3, 2));
                string dbEventAMPM = dbEventTime.Substring(6, 2);

                //  Determine Simplified Event Time for database event
                double dbEventTimeSimplifiedHour = dbEventHour;
                double dbEventTimeSimplifiedMinute = dbEventMinute / 60;
                double dbEventTimeSimplifiedAMPM = dbEventAMPM == "AM" ? 0 : 12;
                if (dbEventHour == 12)
                {
                    dbEventTimeSimplifiedAMPM += 12;
                    dbEventTimeSimplifiedAMPM %= 24;
                }
                double dbEventTimeSimplified = dbEventTimeSimplifiedHour + dbEventTimeSimplifiedMinute + dbEventTimeSimplifiedAMPM;


                //  Check if the events conflict
                //  The new event starts during the old event:
                bool newStartsDuringOld = eventTimeSimplified >= dbEventTimeSimplified && eventTimeSimplified < dbEventTimeSimplified + dbEventLength;

                //  The old event starts during the new event:
                bool oldStartsDuringNew = dbEventTimeSimplified >= eventTimeSimplified && dbEventTimeSimplified < eventTimeSimplified + eventLength;

                //  There are conflicts
                if (newStartsDuringOld || oldStartsDuringNew)
                {
                    //  Close possible conflicting event reader
                    reader.Close();

                    //  GOTO: conflicts error screen
                    panelAddEvent.Visible = false;
                    panelAddEventErrorConflicts.Visible = true;
                    return;
                }
            }
            //  There are no conflicts; close conflicting event reader
            reader.Close();

            //  Get most recent eventID by getting all eventIDs sorted descending
            int mostRecentEventID;
            string commandStrGetMostRecentEventID = "SELECT eventID FROM 834_group5_event ORDER BY eventID DESC";
            MySqlCommand commandGetMostRecentEventID = new MySqlCommand(commandStrGetMostRecentEventID, conn);

            //  Execute query to determine most recent eventID
            reader = commandGetMostRecentEventID.ExecuteReader();

            //  If there are no events, set most recent event ID to 100
            if(!reader.Read())
            {
                mostRecentEventID = 100;
            }
            //  Otherwise, set it to the first value of the retrieved events
            else
            {
                mostRecentEventID = reader.GetInt32(0);
            }

            //  Close most recent eventID reader
            reader.Close();

            //  INSERT command to add the event to the database
            string commandStrAddEventToDB = "INSERT INTO 834_group5_event VALUES (@eID, @eCreatorID, \'personal\', @eTime, @eLength, @eName, @eDesc, @eDate, null)";
            MySqlCommand commandAddEventToDB = new MySqlCommand(commandStrAddEventToDB, conn);
            commandAddEventToDB.Parameters.AddWithValue("@eID", mostRecentEventID + 1);
            commandAddEventToDB.Parameters.AddWithValue("@eCreatorID", uID);
            commandAddEventToDB.Parameters.AddWithValue("@eTime", eventTime);
            commandAddEventToDB.Parameters.AddWithValue("@eLength", eventLength);
            commandAddEventToDB.Parameters.AddWithValue("@eName", eventName);
            commandAddEventToDB.Parameters.AddWithValue("@eDesc", eventDescription);
            commandAddEventToDB.Parameters.AddWithValue("@eDate", eventDate);

            //  Execute INSERT command
            commandAddEventToDB.ExecuteNonQuery();

            //  Close conenction to database
            conn.Close();

            //  Reset "Add Event" Panel
            textBox6.Text = string.Empty;
            textBox7.Text = string.Empty;
            textBox8.Text = string.Empty;
            textBox10.Text = string.Empty;
            comboBox3.Text = string.Empty;

            //  Reset hour and minute textboxes to placeholder values and formatting
            textBox9.ForeColor = Color.Gray;
            textBox9.Text = "1-12...";
            textBox20.ForeColor = Color.Gray;
            textBox20.Text = "0-59...";

            //  GOTO: Add Event Success Panel
            panelAddEvent.Visible = false;
            panelAddEventSuccess.Visible = true;
        }

        //  Event Handler: Return to Add Event Screen (Independent of Panel)
        private void ReturnToAddEventEvent(object sender, EventArgs e)
        {
            //  Get parent panel for the calling button
            Control s = sender as Control;
            Control panel = s.Parent.Parent;

            //  Return to Add Event Screen
            panel.Visible = false;
            panelAddEvent.Visible = true;
        }

        //  Event Handler: Validate input when user leaves eventHour textbox (Add Event Panel)
        private void textBox9_Leave(object sender, EventArgs e)
        {
            bool invalidHour = !Int32.TryParse(textBox9.Text, out int hour) || hour < 1 || hour > 12;

            //  If a valid input is detected, don't reset textbox
            if (!invalidHour)
            {
                return;
            }

            textBox9.ForeColor = Color.Gray;
            textBox9.Text = "1-12...";
        }

        //  Event Handler: Validate input when user leaves eventMinute textbox (Add Event Panel)
        private void textBox20_Leave(object sender, EventArgs e)
        {
            bool invalidMinute = !Int32.TryParse(textBox20.Text, out int minute) || minute < 0 || minute > 59;

            //  If a valid input is detected, don't reset textbox
            if (!invalidMinute)
            {
                return;
            }

            textBox20.ForeColor = Color.Gray;
            textBox20.Text = "0-59...";
        }

        //  Event Handler: Reset eventHour textBox when user clicks on it (Add Event Panel)
        private void textBox9_Click(object sender, EventArgs e)
        {
            textBox9.ForeColor = Color.Black;
            textBox9.Text = string.Empty;
        }

        //  Event Handler: Reset eventMinute textBox when user clicks on it (Add Event Panel)
        private void textBox20_Click(object sender, EventArgs e)
        {
            textBox20.ForeColor = Color.Black;
            textBox20.Text = string.Empty;
        }

        //  Event Handler: Set event date in add event screen based on selected date in monthCalendar2 (Add Event Panel)
        private void monthCalendar2_DateSelected(object sender, DateRangeEventArgs e)
        {
            textBox8.Text = monthCalendar2.SelectionStart.ToShortDateString();
            monthCalendar2.Visible = false;
        }

        //  Event Handler: Show Event Date Select calendar when clicking on event date textbox (Add Event Panel)
        private void textBox8_Click(object sender, EventArgs e)
        {
            monthCalendar2.Visible = true;
            textBox8.Text = "Select Date from Calendar...";
        }


        //  ADD EVENT SUCCESS PANEL
        //  Event Handler: Add Another Event Button (Add Event Success Panel)
        private void button11_Click_1(object sender, EventArgs e)
        {
            //  Reset "Add Event" Panel
            textBox6.Text = string.Empty;
            textBox7.Text = string.Empty;
            textBox8.Text = string.Empty;
            textBox10.Text = string.Empty;
            comboBox3.Text = string.Empty;

            //  Reset hour and minute textboxes to placeholder values and formatting
            textBox9.ForeColor = Color.Gray;
            textBox9.Text = "1-12...";
            textBox20.ForeColor = Color.Gray;
            textBox20.Text = "0-59...";

            //  GOTO: Add event panel
            panelAddEventSuccess.Visible = false;
            panelAddEvent.Visible = true;
        }

        //  Event Handler: Return to Main Menu Button (Add Event Success Panel)
        private void button12_Click(object sender, EventArgs e)
        {
            //  Reload monthly event list
            this.events = new List<Event>();
            RetrieveListOfEvents();
            LoadEventList();

            //  GOTO: Main Menu Panel
            panelAddEventSuccess.Visible=false ;
            splitContainer2.Visible=true ;
        }



        //  DELETE EVENT PANEL
        //  Event Handler: Delete Event Button (Delete Event Panel)
        private void button13_Click(object sender, EventArgs e)
        {
            if (checkedListBox1.CheckedItems.Count == 0)
            {
                MessageBox.Show("Please select an event to delete.");
                return;
            }
            EventItem selected = checkedListBox1.CheckedItems[0] as EventItem;
            Event ev = getEventById(selected.EventID);
                eventToDelete = ev;

                // Step 4: Check group permissions
                if (eventToDelete.eventType == "group")
                {
                    if (accountType == "manager")
                    {
                        splitContainer7.Visible = false;
                        splitContainer3.Visible = true;
                    }
                    else
                    {
                        splitContainer7.Visible = false;
                        splitContainer8.Visible = true; // unauthorized error panel
                    }
                }
                else
                {
                    // Personal event, proceed
                    splitContainer7.Visible = false;
                    splitContainer3.Visible = true;
                }   

        }

        //  Event Handler: Return to Main Menu (Delete Event Panel)
        private void button32_Click(object sender, EventArgs e)
        {
            splitContainer7.Visible = false;
            splitContainer2.Visible = true;
        }


        //  DELETE EVENT CONFIRMATION PANEL
        //  Event Handler: Delete Button Click (Delete Event Confirmation Panel)
        private void button29_Click(object sender, EventArgs e)
        {
            if (eventToDelete == null)
            {
                MessageBox.Show("No event selected to delete. Please go back and select an event.");
                splitContainer3.Visible = false;
                splitContainer2.Visible = true;
                return;
            }

            try
            {
                string connStr = "server=csitmariadb.eku.edu;user=student;database=csc340_db;port=3306;password=Maroon@21?;";
                int affected = 0;

                using (MySqlConnection conn = new MySqlConnection(connStr))
                {
                    conn.Open();
                    string deleteQuery;

                    string rawDate = eventToDelete.eventDate.ToString();
                    string time = eventToDelete.eventTime.ToString();

                    string formattedDate = "";
                    if (DateTime.TryParse(rawDate, out DateTime parsedDate))
                    {
                        formattedDate = parsedDate.ToString("yyyy-MM-dd");
                    }

                    if (eventToDelete.attendees != null && eventToDelete.attendees != string.Empty)
                    {
                        deleteQuery = "DELETE FROM 834_group5_event WHERE eventDate = @date " +
                               "AND eventTime = @time " +
                               "AND eventType = 'group'";

                        MySqlCommand cmdAttendees = new MySqlCommand(deleteQuery, conn);
                        cmdAttendees.Parameters.AddWithValue("@date", formattedDate);
                        cmdAttendees.Parameters.AddWithValue("@time", eventToDelete.eventTime.ToString());

                        affected = cmdAttendees.ExecuteNonQuery();
                    }

                    else
                    {
                        deleteQuery = "DELETE FROM 834_group5_event WHERE eventID = @eID";
                        MySqlCommand cmd = new MySqlCommand(deleteQuery, conn);
                        cmd.Parameters.AddWithValue("@eID", eventToDelete.eventID);
                        affected = cmd.ExecuteNonQuery();
                    }


                    if (affected > 0)
                    {
                        events.RemoveAll(x => x.eventID == eventToDelete.eventID);
                        LoadEventList(); // refresh list
                    }
                }

                eventToDelete = null;
                splitContainer3.Visible = false;
                splitContainer4.Visible = true;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        //  Event Handler: Return to Delete Event Panel (Delete Event Confirmation Panel)
        private void button30_Click(object sender, EventArgs e)
        {
            splitContainer3.Visible = false;
            splitContainer7.Visible = true;
        }


        //  DELETE EVENT SUCCESS PANEL
        //  Event Handler: Return to Main Menu (Delete Event Success Panel)
        private void button31_Click(object sender, EventArgs e)
        {
            splitContainer4.Visible = false;
            splitContainer2.Visible = true;
        }


        //  DELETE EVENT ERROR PANEL
        //  Event Handler: Return to Main Menu Button (Delete Event Error Panel)
        private void button14_Click(object sender, EventArgs e)
        {
            splitContainer2.Visible = true;
            splitContainer8.Visible = false;
        }


        //  EDIT EVENT SELECT PANEL
        //  Event Handler: Edit Event Button (Edit Event Select Panel)
        private Event eventToEdit;
        private void button33_Click(object sender, EventArgs e)
        {
            if (checkedListBox6.CheckedItems.Count == 0)
            {
                MessageBox.Show("⚠️ Please select an event to edit.");
                return;
            }

            EventItem selected = checkedListBox6.CheckedItems[0] as EventItem;
            Event ev = getEventById(selected.EventID);
            eventToEdit = ev;

            //Populate Edit Form fields
            textBox11.Text = eventToEdit.eventName;
            textBox12.Text = DateTime.Parse(eventToEdit.eventDate).ToString("yyyy-MM-dd");
            textBox13.Text = eventToEdit.eventTime;
            textBox14.Text = eventToEdit.eventLength.ToString() + " hours";

            // Permission check
            if (eventToEdit.eventType == "group")
            {
                if (accountType == "manager")
                {

                    //Navigate to edit form 
                    splitContainer1.Visible = false;
                    splitContainer9.Visible = true;
                }
                else
                {

                    splitContainer1.Visible = false;
                    splitContainer8.Visible = true; // Unauthorized error
                }
            }
            else
            {
                //Personal event: go to edit screen
                splitContainer1.Visible = false;
                splitContainer9.Visible = true;
            }
        }

        //  Event Handler: Return to Main Menu (Edit Event Select Panel)
        private void button36_Click(object sender, EventArgs e)
        {
            splitContainer1.Visible = false;
            splitContainer2.Visible = true;
        }


        //  EDIT EVENT PANEL
        //  Event Handler: Return to Edit Event Select Panel (Edit Event Panel)
        private void button35_Click(object sender, EventArgs e)
        {
            splitContainer9.Visible = false;
            splitContainer1.Visible = true;
        }
        
        //  Event Handler: Edit Event Button (Edit Event Panel)
        private void button15_Click_1(object sender, EventArgs e)
        {
            if (eventToEdit == null)
            {
                MessageBox.Show("No event selected to update.");
                return;
            }

            try
            {
                // Get updated values from the Edit Form fields
                string updatedName = textBox11.Text.Trim();
                string updatedDate = textBox12.Text.Trim();  // Make sure format is yyyy-MM-dd
                string updatedTime = textBox13.Text.Trim();
                string updatedLengthStr = textBox14.Text.Trim();

                if (string.IsNullOrEmpty(updatedName) || string.IsNullOrEmpty(updatedDate) ||
                    string.IsNullOrEmpty(updatedTime) || string.IsNullOrEmpty(updatedLengthStr))
                {
                    MessageBox.Show("⚠️ Please fill in all fields before saving.");
                    return;
                }

                // Parse event length 
                double updatedLength = double.Parse(new string(updatedLengthStr.Where(char.IsDigit).ToArray()));

                // Update in database
                string connStr = "server=csitmariadb.eku.edu;user=student;database=csc340_db;port=3306;password=Maroon@21?;";
                using (MySqlConnection conn = new MySqlConnection(connStr))
                {
                    conn.Open();
                    string updateQuery = @"UPDATE 834_group5_event 
                                   SET eventName = @name, eventDate = @date, 
                                       eventTime = @time, eventLength = @length 
                                   WHERE eventID = @id";
                    MySqlCommand cmd = new MySqlCommand(updateQuery, conn);
                    cmd.Parameters.AddWithValue("@name", updatedName);
                    cmd.Parameters.AddWithValue("@date", updatedDate);
                    cmd.Parameters.AddWithValue("@time", updatedTime);
                    cmd.Parameters.AddWithValue("@length", updatedLength);
                    cmd.Parameters.AddWithValue("@id", eventToEdit.eventID);
                    cmd.ExecuteNonQuery();
                }

                // Update local list
                eventToEdit.eventName = updatedName;
                eventToEdit.eventDate = updatedDate;
                eventToEdit.eventTime = updatedTime;
                eventToEdit.eventLength = updatedLength;

                // Refresh event list
                LoadEventList();

                MessageBox.Show("Event updated successfully.");

                // Return to main menu
                splitContainer9.Visible = false;
                splitContainer2.Visible = true;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error while saving: " + ex.Message);
            }
        }


        //  EDIT EVENT SUCCESS PANEL
        //  Event Handler: Return to Main Menu Button (Edit Event Success Panel)
        private void button34_Click(object sender, EventArgs e)
        {
            splitContainer5.Visible = false;
            splitContainer2.Visible = true;
        }



        //  VIEW EVENT PANEL
        //  Event Handler: Return to Main Menu Button (View Event Panel)
        private void button16_Click(object sender, EventArgs e)
        {
            //  GOTO: Main Menu Panel
            splitContainer10.Visible = false;
            splitContainer2.Visible = true;
        }


        
        //  SCHEDULE EVENT ATTENDEES PANEL
        //  Event Handler: Check Attendee Availability Button (Schedule Event Attendees Panel)
        private void button18_Click(object sender, EventArgs e)
        {
            checkedListBox3.Items.Clear();
            splitContainer11.Visible = false;
            splitContainer12.Visible=true ;

            string idString = buildAttendeesList(checkedListBox2);
            List<int> attendeeIds = idString.Split(',').Select(id => int.Parse(id)).ToList();

            List<DateTime> availableSlotsForAll = verifyAvailability(attendeeIds);

            // Only show slots available to ALL selected attendees
            PopulateAvailableSlots(checkedListBox3, availableSlotsForAll);
        }



        //  SCHEDULE EVENT AVAILABILITY PANEL
        //  Event Handler: Confirm Meeting Time Button (Schedule Event Availability Panel)
        private void button19_Click(object sender, EventArgs e)
        {
            List<string> selectedSlots = new List<string>();

            splitContainer12.Visible = false;
            splitContainer13 .Visible=true ;

            checkedListBox4.Items.Clear();
            checkedListBox5.Items.Clear();

            // Collect selected slots
            foreach (var item in checkedListBox3.CheckedItems)
            {
                selectedSlots.Add(item.ToString());
            }

            // Populate attendees list
            foreach (Attendee attendee in attendeesList)
            {
                int index = checkedListBox4.Items.Add(attendee);
                checkedListBox4.SetItemChecked(index, true);
            }
            // set selected slots as checked for confirmation.
            foreach (string selectedSlot in selectedSlots)
            {
                int index = checkedListBox5.Items.Add(selectedSlot);
                checkedListBox5.SetItemChecked(index, true);
            }
        }

        //  Build list of attendees for scheduled event
        private string buildAttendeesList(CheckedListBox selectedItems)
        {
            List<int> selectedAttendeeIds = new List<int>();

            // Clear the existing attendees list before adding new ones to avoid duplication
            this.attendeesList.Clear();

            foreach (var item in selectedItems.CheckedItems)
            {
                if (item is Attendee attendee)
                {
                    selectedAttendeeIds.Add(attendee.Id);
                    this.attendeesList.Add(attendee);
                }
            }

            // Return a comma-separated string of selected attendee IDs for further use
            string idString = string.Join(",", selectedAttendeeIds);
            return idString;
        }

        //  Add availability slots to availability text box for scheduling meetings
        private void PopulateAvailableSlots(CheckedListBox checkedListBox, List<DateTime> availableSlots)
        {
            checkedListBox.Items.Clear();

            foreach (DateTime slot in availableSlots)
            {
                checkedListBox.Items.Add(slot.ToString("yyyy-MM-dd hh:mm tt"));
            }
        }

        //  Determine Availability of all selected users for scheduling event
        private List<DateTime> verifyAvailability(List<int> userIds, int daysAhead = 7, int startHour = 9, int endHour = 17)
        {
            Dictionary<int, HashSet<DateTime>> userBusySlots = new Dictionary<int, HashSet<DateTime>>();
            List<DateTime> availableSlots = new List<DateTime>();
            List<DateTime> excludedBusySlots = new List<DateTime>(); // store conflicts.
            DateTime now = DateTime.Now;

            string connStr = "server=csitmariadb.eku.edu;user=student;database=csc340_db;port=3306;password=Maroon@21?;";

            try
            {
                using (MySqlConnection conn = new MySqlConnection(connStr))
                {
                    conn.Open();

                    foreach (int uid in userIds)
                    {
                        string sql = @"
                                            SELECT eventDate, eventTime
                                            FROM 834_group5_event
                                            WHERE STR_TO_DATE(CONCAT(eventDate, ' ', eventTime), '%Y-%m-%d %h:%i %p') >= NOW()
                                              AND eventCreatorID = @uid;
                                        ";

                        HashSet<DateTime> busySlots = new HashSet<DateTime>();

                        using (MySqlCommand cmd = new MySqlCommand(sql, conn))
                        {
                            cmd.Parameters.AddWithValue("@uid", uid);

                            using (MySqlDataReader reader = cmd.ExecuteReader())
                            {
                                while (reader.Read())
                                {
                                    DateTime eventDate = reader.GetDateTime(reader.GetOrdinal("eventDate"));
                                    string formattedDate = eventDate.ToString("yyyy-MM-dd");

                                    string timeRaw = reader["eventTime"].ToString(); // should be like "02:30 PM"
                                    string combined = $"{formattedDate} {timeRaw}"; // ex: "2025-05-26 02:30 PM"

                                    if (DateTime.TryParseExact(combined, "yyyy-MM-dd hh:mm tt",
                                                               CultureInfo.InvariantCulture, DateTimeStyles.None,
                                                               out DateTime busySlot))
                                    {
                                        // Normalize to zero seconds
                                        busySlot = new DateTime(busySlot.Year, busySlot.Month, busySlot.Day, busySlot.Hour, busySlot.Minute, 0);
                                        busySlots.Add(busySlot);
                                    }
                                    else
                                    {
                                        Debug.WriteLine($"Failed to parse: {combined}");
                                    }
                                }


                            }
                        }

                        userBusySlots[uid] = busySlots;
                    }
                }

                // Generate all candidate 30-minute slots
                List<DateTime> candidateSlots = new List<DateTime>();
                for (int day = 0; day < daysAhead; day++)
                {
                    DateTime baseDate = now.Date.AddDays(day);

                    for (int hour = startHour; hour < endHour; hour++)
                    {
                        for (int minute = 0; minute < 60; minute += 30)
                        {
                            DateTime slot = new DateTime(baseDate.Year, baseDate.Month, baseDate.Day, hour, minute, 0);
                            if (slot > now)
                                candidateSlots.Add(slot);
                        }
                    }
                }

                // Validate candidate slots against ALL users' busy times
                foreach (DateTime slot in candidateSlots)
                {
                    bool allAvailable = true;

                    foreach (var kvp in userBusySlots)
                    {
                        if (kvp.Value.Contains(slot))
                        {
                            allAvailable = false;
                            excludedBusySlots.Add(slot);
                            break;
                        }
                    }

                    if (allAvailable)
                    {
                        availableSlots.Add(slot);
                    }
                }

                // Show message if there were any busy slots
                if (excludedBusySlots.Count > 0)
                {
                    string message = "The following time slots are not available due to scheduling conflicts:\n\n" +
                                     string.Join("\n", excludedBusySlots.Select(dt => dt.ToString("yyyy-MM-dd hh:mm tt")));
                    MessageBox.Show(message, "Conflicting Time Slots", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error generating group availability: " + ex.Message);
            }

            return availableSlots;
        }



        //  SCHEDULE EVENT CONFIRMATION PANEL
        //  Event Handler: Confirm Scheduled Meeting Button (Schedule Event Confirmation Panel)
        private void button20_Click(object sender, EventArgs e)
        {
            string idString = buildAttendeesList(checkedListBox4);
            List<Event> eventsList = new List<Event>();

            //Events for the manager block
            foreach (var slot in checkedListBox5.CheckedItems)
            {
                Event myEvent = new Event();
                myEvent.eventID = -1;
                myEvent.eventCreatorID = uID;
                myEvent.eventType = "group";

                if (DateTime.TryParseExact(slot.ToString(), "yyyy-MM-dd hh:mm tt", CultureInfo.InvariantCulture, DateTimeStyles.None, out DateTime parsedSlot))
                {
                    myEvent.eventDate = parsedSlot.ToString("yyyy-MM-dd");
                    myEvent.eventTime = parsedSlot.ToString("hh:mm tt");
                }

                myEvent.eventLength = 0.5;
                myEvent.eventName = "Team Meeting";
                myEvent.eventDescription = "Team meeting scheduled by management.";
                myEvent.attendees = idString;
                eventsList.Add(myEvent);
            }

            // Events for the attendees so it is blocked and tracked.
            foreach (Attendee attendee in checkedListBox4.CheckedItems)
            {
                foreach (var slot in checkedListBox5.CheckedItems)
                {
                    Event myEvent = new Event();
                    myEvent.eventID = -1;
                    myEvent.eventCreatorID = attendee.Id;
                    myEvent.eventType = "group";

                    if (DateTime.TryParseExact(slot.ToString(), "yyyy-MM-dd hh:mm tt", CultureInfo.InvariantCulture, DateTimeStyles.None, out DateTime parsedSlot))
                    {
                        myEvent.eventDate = parsedSlot.ToString("yyyy-MM-dd");
                        myEvent.eventTime = parsedSlot.ToString("hh:mm tt");
                    }

                    myEvent.eventLength = 0.5;
                    myEvent.eventName = "Team Meeting";
                    myEvent.eventDescription = "Team meeting scheduled by management.";
                    myEvent.attendees = idString;
                    eventsList.Add(myEvent);
                }
            }

            saveEvents(eventsList);
        }

        //  Save list of events to database
        private void saveEvents(List<Event> MyEvents)
        {
            string connStr = "server=csitmariadb.eku.edu;user=student;database=csc340_db;port=3306;password=Maroon@21?;";
            MySqlConnection conn = new MySqlConnection(connStr);

            //  Get eventID
            int mostRecentEventID;
            string commandStrGetMostRecentEventID = "SELECT eventID FROM 834_group5_event ORDER BY eventID DESC";
            MySqlCommand commandGetMostRecentEventID = new MySqlCommand(commandStrGetMostRecentEventID, conn);

            conn.Open();
            MySqlDataReader reader = commandGetMostRecentEventID.ExecuteReader();
            if (!reader.Read())
            {
                mostRecentEventID = 100;
            }
            else
            {
                mostRecentEventID = reader.GetInt32(0);
            }
            reader.Close();


            foreach (var MyEv in MyEvents)
            {
                string commandStrAddEventToDB = "INSERT INTO 834_group5_event VALUES (@eID, @eCreatorID, @evType, @eTime, @eLength, @eName, @eDesc, @eDate, @evAttend)";
                MySqlCommand commandAddEventToDB = new MySqlCommand(commandStrAddEventToDB, conn);

                commandAddEventToDB.Parameters.AddWithValue("@eID", ++mostRecentEventID);
                commandAddEventToDB.Parameters.AddWithValue("@eCreatorID", MyEv.eventCreatorID);
                commandAddEventToDB.Parameters.AddWithValue("@evType", MyEv.eventType);
                commandAddEventToDB.Parameters.AddWithValue("@eTime", MyEv.eventTime);
                commandAddEventToDB.Parameters.AddWithValue("@eLength", MyEv.eventLength);
                commandAddEventToDB.Parameters.AddWithValue("@eName", MyEv.eventName);
                commandAddEventToDB.Parameters.AddWithValue("@eDesc", MyEv.eventDescription);
                commandAddEventToDB.Parameters.AddWithValue("@eDate", MyEv.eventDate);
                commandAddEventToDB.Parameters.AddWithValue("@evAttend", MyEv.attendees);

                commandAddEventToDB.ExecuteNonQuery();
            }

            conn.Close();
            MessageBox.Show("Your event(s) have been created.");

            this.attendeesList.Clear();

            splitContainer13.Visible = false;
            splitContainer2.Visible = true;

            checkedListBox1.Items.Clear();
            this.events.Clear();

            RetrieveListOfEvents();
            LoadEventList();
        }


        //  GENERAL FUNCTIONS
        //  Select all events that the user is a part of from the database
        private void RetrieveListOfEvents()
        {
            try
            {

                string connStr = "server=csitmariadb.eku.edu;user=student;database=csc340_db;port=3306;password=Maroon@21?;";
                using (MySqlConnection conn = new MySqlConnection(connStr))
                {
                    conn.Open();

                    string sql = "SELECT * FROM 834_group5_event WHERE eventCreatorID = @uid ORDER BY eventDate ASC;";
                    MySqlCommand cmd = new MySqlCommand(sql, conn);
                    cmd.Parameters.AddWithValue("@uid", uID);

                    using (MySqlDataReader reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            Event myEvent = new Event();
                            myEvent.eventID = (int)reader["eventID"];
                            myEvent.eventCreatorID = (int)reader["eventCreatorID"];
                            myEvent.eventType = reader["eventType"].ToString();
                            myEvent.eventTime = reader["eventTime"].ToString();
                            myEvent.eventLength = (double)reader["eventLength"];
                            myEvent.eventName = reader["eventName"].ToString();
                            myEvent.eventDescription = reader["eventDescription"].ToString();
                            myEvent.eventDate = reader["eventDate"].ToString();
                            myEvent.attendees = reader["attendees"].ToString();

                            this.events.Add(myEvent);  
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error loading events: " + ex.Message);
            }
        }

        //  Add all events the user is a part of to the monthly event list
        private void LoadEventList()
        {
            listBox1.Items.Clear();
            if (this.events.Count > 0)
            {
                foreach (Event item in this.events)
                {
                    int id = item.eventID;
                    string name = item.eventName.ToString();
                    string rawDate = item.eventDate.ToString();
                    string time = item.eventTime.ToString();

                    string formattedDate;

                    if (DateTime.TryParse(rawDate, out DateTime parsedDate))
                    {
                        formattedDate = parsedDate.ToString("MM/dd/yyyy");
                    }
                    else
                    {
                        formattedDate = "Invalid Date";
                    }

                    string display = $"{formattedDate} {time} - {name}";
                    listBox1.Items.Add(new EventItem { EventID = id, Display = display });
                }
            }

        }

        //  Select event from locally-stored list of events by event ID
        private Event getEventById(int id)
        {
            var found = this.events.FirstOrDefault(e => e.eventID == id);

            if (found == null)
            {
                MessageBox.Show("Item Not Found");
                return null;
            }
            return found;
        }
    }
}

//  Locally stored (truncated) event objects.
class EventItem
{
    public int EventID { get; set; }
    public int eventCreatorID { get; set; }
    public string Display { get; set; }

    public override string ToString()
    {
        return Display;
    }
}

//  Objects for keeping track of users being added to group meetings
public class Attendee
{
    public int Id { get; set; }
    public string Name { get; set; }

    public override string ToString()
    {
        return Name;
    }
}