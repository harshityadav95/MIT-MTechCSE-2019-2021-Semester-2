using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceModel;
using System.Web;

namespace WcfService1.Models
{
    [MessageContract]
    public class GateGradeResponse
    {
        [MessageHeader]
        public string UserName { get; set; }

        [MessageBodyMember]
        public string RegisterNo { get; set; }

        [MessageBodyMember]
        public string Term { get; set; }

        [MessageBodyMember]
        public string Grade { get; set; }
    }
}