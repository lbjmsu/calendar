using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
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
        private EventItem selectedEvent;
        private int uID;
        private string accountType;

        public Form1()
        {
            InitializeComponent();
            RetrieveListOfEvents();
            LoadEventList();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //  Login Button Click
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

            conn.Close();
        }

        //  Create Account Button Click
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
                reader.Close();

                //  Create query to return most recent uID
                string commandStrMostRecentUID = "SELECT uid FROM 834_group5_user ORDER BY uid DESC";
                MySqlCommand cmdMostRecentUID = new MySqlCommand(commandStrMostRecentUID, conn);

                //  Read and store the most recent uID
                reader = cmdMostRecentUID.ExecuteReader();
                reader.Read();
                int mostRecentUID = reader.GetInt32(0);

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

                //  GOTO: login screen
                ReturnToLoginEvent(sender, e);
            }

            conn.Close();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            splitContainer2.Visible=false;
            splitContainer1.Visible=true;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem is EventItem selectedEvent)
            {
                splitContainer2.Visible = false;
                splitContainer10.Visible = true;

                Event found = getEventById(selectedEvent.EventID);

                textBox15.Text = found.eventName.ToString();
                textBox16.Text = found.eventDescription.ToString();
                textBox17.Text = found.eventDate.ToString();
                textBox18.Text = found.eventTime.ToString();
                textBox19.Text = found.eventType.ToString();
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            panelLogin.Visible=false;
            panelCreateAccount.Visible=true;
        }

        

        private void button11_Click(object sender, EventArgs e)
        {
            splitContainer6.Visible=false;
            splitContainer5.Visible=true;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            splitContainer5.Visible = false;
            splitContainer6.Visible=true;
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            splitContainer2.Visible=false ;
            splitContainer5.Visible=true ;
        }

        private void button11_Click_1(object sender, EventArgs e)
        {
            splitContainer6.Visible = false ;
            splitContainer5.Visible=true ;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            splitContainer6.Visible=false ;
            splitContainer2.Visible=true ;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            splitContainer7.Visible=false ;
            splitContainer9.Visible=true ;
        }

        private void button15_Click(object sender, EventArgs e)
        {
            splitContainer8.Visible = false ;
            splitContainer7.Visible=true ;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            splitContainer2.Visible = false ;
            splitContainer7.Visible = true;
        }

        private void splitContainer8_Panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {
            splitContainer2.Visible = true;
            splitContainer8.Visible=false ;
        }

        private void label21_Click(object sender, EventArgs e)
        {

        }

        private void label22_Click(object sender, EventArgs e)
        {

        }

        private void label23_Click(object sender, EventArgs e)
        {

        }

        private void label24_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click_1(object sender, EventArgs e)
        {
            splitContainer9.Visible = false;
            splitContainer8 .Visible=true ;
        }

        private void splitContainer10_Panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void label28_Click(object sender, EventArgs e)
        {

        }

        private void label27_Click(object sender, EventArgs e)
        {

        }

        private void label26_Click(object sender, EventArgs e)
        {

        }

        private void label29_Click(object sender, EventArgs e)
        {

        }

        private void label30_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {
            splitContainer10.Visible = false;
            splitContainer2 .Visible=true ;
        }

        private void label19_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {
            splitContainer2.Visible = false;
            splitContainer11 .Visible=true ;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            splitContainer11.Visible = false;
            splitContainer12.Visible=true ;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            splitContainer12.Visible = false;
            splitContainer13 .Visible=true ;
        }

        private void checkedListBox3_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void monthCalendar1_DateChanged(object sender, DateRangeEventArgs e)
        {

        }

        //private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        //{
        //    if (listBox1.SelectedItem != null)
        //    {
        //        this.selectedEvent = (EventItem)listBox1.SelectedItem;

        //    }
        //}

        //// This implements the selectEvent action for the user.
        //private void listBox1_DoubleClick(object sender, EventArgs e)
        //{
        //    if (listBox1.SelectedItem != null)
        //    {
        //        this.selectedEvent = (EventItem)listBox1.SelectedItem;

        //    }
        //}

        /*
         * Retrieve all current events.
         */
        private void RetrieveListOfEvents()
        {
            try
            {

                string connStr = "server=csitmariadb.eku.edu;user=student;database=csc340_db;port=3306;password=Maroon@21?;";
                using (MySqlConnection conn = new MySqlConnection(connStr))
                {
                    conn.Open();

                    string sql = "SELECT * FROM 834_group5_event ORDER BY eventDate ASC;";
                    MySqlCommand cmd = new MySqlCommand(sql, conn);
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

        //  Click the "return to login screen" button on a login error screen.
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

        //  Click the "back" button on the create account error screen
        private void ReturnToCreateAccountEvent(object sender, EventArgs e)
        {
            //  Get parent panel for the calling button
            Control s = sender as Control;
            Control panel = s.Parent.Parent;

            //  Reset password textboxes
            textBox4.Text = string.Empty;
            textBox5.Text = string.Empty;

            //  Return to Login Screen
            panel.Visible = false;
            panelCreateAccount.Visible = true;
        }
    }
}

class EventItem
{
    public int EventID { get; set; }
    public string Display { get; set; }

    public override string ToString()
    {
        return Display;
    }
}