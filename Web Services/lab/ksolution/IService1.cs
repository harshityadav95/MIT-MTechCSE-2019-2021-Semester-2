using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using WcfService1.Models;

namespace WcfService1
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the interface name "IService1" in both code and config file together.
    [ServiceContract]
    public interface IService1
    {
        [OperationContract]
        GetResultResponse GetResult(string RegisterNo, int semester, string term);

        [OperationContract]
        GetGradeResponse GetGradeWithCredentials(GetGradeRequest request);

        [OperationContract]
        GetCabResponse Getcabs(GetCabRequest request);
    }

    [MessageContract]
    public class GetCabRequest
    {
        [MessageHeader]
        public String Username { get; set; }

        [MessageBodyMember]
        public int lattitude { get; set; }

        [MessageBodyMember]
        public int longitude { get; set; }
    }

    [MessageContract]
    public class GetCabResponse
    {
        [MessageBodyMember]
        public String ETA { get; set; }

        [MessageBodyMember]
        public String CarType { get; set; }
    }


}
