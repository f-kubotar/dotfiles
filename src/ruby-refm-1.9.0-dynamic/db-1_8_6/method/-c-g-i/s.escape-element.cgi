visibility=public
kind=defined
names=escapeElement

--- escapeElement(string, *elements)

elements �˻��ꤷ��������ȤΥ�����������λ��Ȥ��ִ����ޤ���

        �㡧
        p CGI.escapeElement('<BR><A HREF="url"></A>', "A", "IMG")
             # => "<BR>&lt;A HREF="url"&gt;&lt;/A&gt"

        p CGI.escapeElement('<BR><A HREF="url"></A>', ["A", "IMG"])
             # => "<BR>&lt;A HREF="url"&gt;&lt;/A&gt"

