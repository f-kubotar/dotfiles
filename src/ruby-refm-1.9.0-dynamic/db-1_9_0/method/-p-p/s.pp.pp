visibility=public
kind=defined
names=pp

--- pp(obj, out = $>, width = 79)    -> object
obj �� out ���� width �� pretty print ���ޤ���
out ���֤��ޤ���

@param obj ɽ�����������֥������Ȥ���ꤷ�ޤ���

@param out ���������ꤷ�ޤ���<< �᥽�åɤ��������Ƥ���ɬ�פ�����ޤ���

@param width �������������ꤷ�ޤ���

  str = PP.pp([[:a, :b], [:a, [[:a, [:a, [:a, :b]]], [:a, :b],]]], '', 20)
  puts str
  #=>
  [[:a, :b],
   [:a,
    [[:a,
      [:a, [:a, :b]]],
     [:a, :b]]]]

