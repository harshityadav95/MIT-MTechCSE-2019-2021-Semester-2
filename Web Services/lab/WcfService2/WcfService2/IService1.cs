using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using WcfService2.Models;

namespace WcfService2
{
    [ServiceContract]
    public interface IService1
    {
        [OperationContract]
        GetCabDetailsResponse GetCabDetails(int latitude, int longitude);

        [OperationContract]
        GetCabResponse GetCabDetailsWithCredentials(GetCabRequest request);
    }

}
