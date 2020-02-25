using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ServiceModel;


namespace WcfService2.Models
{
    [MessageContract]
    public class GetCabRequest
    {
        [MessageHeader]
        public string UserName { get; set; }

        [MessageBodyMember]
        public int Latitude { get; set; }

        [MessageBodyMember]
        public int Longitude { get; set; }
    }
}