visibility=public
kind=defined
names=params

--- params

�ѥ�᡼�����Ǽ�����ϥå�����֤��ޤ���

�ե����फ�����Ϥ��줿�ͤ䡢URL�������ޤ줿 QUERY_STRING �Υѡ�����̤μ����ʤɤ˻��Ѥ��ޤ���

      cgi = CGI.new
      cgi.params['developer']     # => ["Matz"] (Array)
      cgi.params['developer'][0]  # => "Matz"
      cgi.params['']              # => nil

