visibility=public
kind=defined
names=unescapeElement

--- unescapeElement(string, *element)
��������Ǥ�����HTML���������פ����᤹��

        �㡧
        print CGI.unescapeElement('&lt;BR&gt;&lt;A HREF="url"&gt;&lt;/A&gt;', "A", "IMG")
          # => "&lt;BR&gt;<A HREF="url"></A>"

        print CGI.unescapeElement('&lt;BR&gt;&lt;A HREF="url"&gt;&lt;/A&gt;', %w(A IMG))
          # => "&lt;BR&gt;<A HREF="url"></A>"

