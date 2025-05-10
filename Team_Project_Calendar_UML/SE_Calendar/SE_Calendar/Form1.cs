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

        public Form1()
        {
            InitializeComponent();
            RetrieveListOfEvents();
            LoadEventList();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            splitContainer1.Visible = false;
            splitContainer2.Visible = true;
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
            splitContainer1.Visible=false;
            splitContainer3.Visible=true;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            splitContainer3.Visible = false;
            splitContainer4.Visible=true;
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