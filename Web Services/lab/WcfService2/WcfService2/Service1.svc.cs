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
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the class name "Service1" in code, svc and config file together.
    // NOTE: In order to launch WCF Test Client for testing this service, please select Service1.svc or Service1.svc.cs at the Solution Explorer and start debugging.
    public class Service1 : IService1
    {
        public GetCabDetailsResponse GetCabDetails(int latitude, int longitude)
        {
            GetCabDetailsResponse response
                = new GetCabDetailsResponse(1, DateTime.Now, "SUV");
            return response;
        }

        public GetCabResponse GetCabDetailsWithCredentials(GetCabRequest request)
        {
            var response = new GetCabResponse();
            response.ETA = DateTime.Now;
            response.CabType = "SUV";
            return response;
        }   
    }
}
