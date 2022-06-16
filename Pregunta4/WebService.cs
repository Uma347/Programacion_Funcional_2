using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

/// <summary>
/// Descripción breve de WebService
/// </summary>
[WebService(Namespace = "http://tempuri.org/")]
[WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]

public class WebService : System.Web.Services.WebService
{

    public WebService()
    {

    }

    [WebMethod]
    public string HelloWorld()
    {
        return "Hola a todos";
    }

    [WebMethod]
    public string fibrec(int a)
    {
        return Library1.modfibos.generafibo3(a);
    }

    [WebMethod]
    public string fibest(int a)
    {
        return Library1.modfibos.fib3(a);
    }
}