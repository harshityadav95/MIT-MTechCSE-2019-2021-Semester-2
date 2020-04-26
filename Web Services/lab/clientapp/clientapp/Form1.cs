using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


namespace clientapp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void btnshow_Click(object sender, EventArgs e)
        {
            
            regcheck.Text = txtregisterno.Text;
            var client = new ServiceReference1.Service1Client();
            ServiceReference1.GetResultResponse response=client.GetResult(txtregisterno.Text, 6, "ABC");
           MessageBox.Show(response.registerNo + " " + response.grade);
        }
    }
}
