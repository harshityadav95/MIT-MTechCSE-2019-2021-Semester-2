using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceModel;
using System.Web;

namespace WcfService2.Models
{
    [MessageContract]
    public class GetGradeResponse
    {
        [MessageHeader]
        public string UserName { get; set; }

        [MessageBodyMember]
        public string RegisterNo { get; set; }

        [MessageBodyMember]
        public string Name { get; set; }

        [MessageBodyMember]
        public string Grade { get; set; }

    }
}