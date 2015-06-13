from http.server import HTTPServer, BaseHTTPRequestHandler
import psutil, datetime
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        cpu_util = psutil.cpu_percent(interval=1, percpu=True)

        mem = psutil.virtual_memory()
        THRESHOLD = 100 * 1024 * 1024

        text="""<html lang="en">
                  <head>
                  </head>
                  <body>
                    <table width="600">
                        <tr id="boot_time" bgcolor="#58FA82" >
                            <td >Boot Time</td>
                            <td>"""
        text=text+str(boot_time)+"""
                            </td>
                        </tr>
                        <tr id="cpu">
                            <td>CPU UTILIZATION</td>
                            <td>
                                <table width="250">"""
        i=1
        for cpu in cpu_util:
            text+="""<tr><td>CPU {core}</td><td bgcolor="#C86FF5">{util} %</td></tr>""".format(core=i,util=cpu)
            i+=1

        text+="""         </table>
                            </td>
                        </tr>
                        <tr id ="availiable_memory" bgcolor="#58FA82">
                            <td>AVAILABLE MEMORY</td>
                            <td>"""
        text=text+str(mem.available)+"""</td>
                        </tr>
                        <tr id="used_memory">
                            <td>USED MEMORY</td>
                            <td>"""
        text=text+str(mem.used)+"""</td>
                        </tr>
                        <tr id="used_percentage" bgcolor="#58FA82">
                            <td>USED PERCENTAGE</td>"""
        if mem.percent<50:
            text+="<td>"
        else:
            text+="""<td bgcolor="red">"""

        text=text+str(mem.percent)+"""</td>
                        </tr>
                    </table>
                  </body>  
                </html>"""
        self.wfile.write(bytes(text,'utf-8'))
        return

server = HTTPServer(("", 8000), MyHTTPRequestHandler)
server.serve_forever()