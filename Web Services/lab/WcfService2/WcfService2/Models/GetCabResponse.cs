using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceModel;
using System.Web;

namespace WcfService2.Models
{
    [MessageContract]
    public class GetCabResponse
    {
        [MessageBodyMember]
        public DateTime ETA { get; set; }

        [MessageBodyMember]
        public string CabType { get; set; }
    }
}