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
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the class name "Service1" in code, svc and config file together.
    // NOTE: In order to launch WCF Test Client for testing this service, please select Service1.svc or Service1.svc.cs at the Solution Explorer and start debugging.
    public class Service1 : IService1
    {
        public GetResultResponse GetResult(string regNo, int sem, string term)
        {
            GetResultResponse response = new GetResultResponse(1, regNo, "Karthik", "A+");
            //response.RegisterNo = regNo;
            //response.Name = "Karthik";
            //response.Grade = "A+";
            return response;
        }

        public GetGradeResponse GetGradeWithCredentials(GetGradeRequest request)
        {
            var response = new GetGradeResponse();
            response.RegisterNo = request.RegisterNo;
            response.Name = "Karthik";
            response.Grade = "A+";
            return response;
        }

        public GetCabResponse Getcabs(GetCabRequest request)
        {
            var response = new GetCabResponse();
            response.ETA = "876";
            response.CarType = "SUV";
            return response;
        }
    }
}
