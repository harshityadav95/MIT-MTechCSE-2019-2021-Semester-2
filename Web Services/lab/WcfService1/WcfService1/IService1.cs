﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;

namespace WcfService1
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the interface name "IService1" in both code and config file together.
    [ServiceContract]
    public interface IService1
    {

        [OperationContract]
        GetResultResponse GetResult(string registerNo, int semester, string term);

    }

    [DataContract]
    public class GetResultResponse
    {
        
        public int ID { get; set; }
        [DataMember]
        public string name { get; set; }
        [DataMember]
        public string registerNo { get; set; }
        [DataMember]
        public string grade { get; set; }

    }
}
