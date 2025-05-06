using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SE_Calendar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
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

        private void splitContainer2_Panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            splitContainer2.Visible=false ;
            splitContainer10.Visible=true;
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

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

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
    }
}
