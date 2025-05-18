using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SE_Calendar
{
    //  Event objects used for processing the addition, deletion, editing, and viewing of events in the database.
    internal class Event
    {
        public int eventID {  get; set; }
        public int eventCreatorID { get; set; }
        public string eventName { get; set; }
        public string eventType { get; set; }
        public double eventLength { get; set; }
        public string eventDescription { get; set; }
        public string eventDate { get; set; }
        public string eventTime { get; set; }
        public string attendees { get; set; }
        public string Display {  get; set; }

        public override string ToString()
        {
            return Display;
        }

    }
}
