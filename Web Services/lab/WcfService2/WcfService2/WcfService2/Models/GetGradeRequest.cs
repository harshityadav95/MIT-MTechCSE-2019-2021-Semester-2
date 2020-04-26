using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ServiceModel;

namespace WcfService2.Models
{
    [MessageContract]
    public class GetGradeRequest
    {

        [MessageHeader]
        public string UserName { get; set; }

        [MessageBodyMember]
        public string RegisterNo { get; set; }

        [MessageBodyMember]
        public int Semester { get; set; }

        [MessageBodyMember]
        public string Grade { get; set; }

    }
}