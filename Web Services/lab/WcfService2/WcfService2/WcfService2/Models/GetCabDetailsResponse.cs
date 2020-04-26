using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.Web;

namespace WcfService2.Models
{
    [DataContract]
    public class GetCabDetailsResponse
    {
        public int Id { get; set; }

        [DataMember]
        public DateTime ETA { get; set; }

        [DataMember]
        public string CabType { get; set; }

        public GetCabDetailsResponse(int id, DateTime eta, string cabType)
        {
            Id = id;
            ETA = eta;
            CabType = cabType;
        }
    }


}