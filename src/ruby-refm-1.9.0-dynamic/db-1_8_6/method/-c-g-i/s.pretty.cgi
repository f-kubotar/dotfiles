visibility=public
kind=defined
names=pretty

--- pretty(string, shift = "  ")

HTML ��ʹ֤˸��䤹���������ޤ���

        �㡧
        print CGI.pretty("<HTML><BODY></BODY></HTML>")
          # <HTML>
          #   <BODY>
          #   </BODY>
          # </HTML>

        print CGI.pretty("<HTML><BODY></BODY></HTML>", "\t")
          # <HTML>
          #         <BODY>
          #         </BODY>
          # </HTML>

