


%�������

% ����ͼ����
G = digraph(A);

% �����ڵ��ǩ
nodeLabels = {'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', ...
              'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'Y'};

% ���ڵ��ǩ�����ͼ����
G.Nodes.Name = nodeLabels';


% ����ͼ�δ���

figure;

% ��������ͼ�����ò���Ϊ�ֲ㲼�֣�������ԭʼ�Ľڵ��ǩ
h = plot(G, 'Layout', 'layered', 'NodeLabel', {});

% �޸Ľڵ��С����ɫ����״
h.MarkerSize = 20;
h.NodeColor = 'r';
h.Marker = 'o';

% �޸��ض��ڵ�Ĵ�С����ɫ����״
highlight(h, [11,6,17,18,5,7,4,9,1,3,13,19], 'NodeColor', [1 0.435 0.589], 'MarkerSize', 10, 'Marker', 'o');  % X1
highlight(h, [2,8,12,10,14,16], 'NodeColor', [1 0.588 0.443], 'MarkerSize', 10 , 'Marker', 'o');  % X1
highlight(h, [15], 'NodeColor', [1 0.780 0.3725], 'MarkerSize', 10, 'Marker', 'o'); % Y
highlight(h, [20], 'NodeColor', [0.3059 0.7098 0.9804], 'MarkerSize', 10, 'Marker', 'p'); % Y

% ��ȡ�ڵ�����
xData = h.XData;
yData = h.YData;

% �ֶ����ӽڵ��ǩ��������ԭʼ�Ľڵ��ǩ


% ���ñߵ�����
h.LineWidth = 1.5;
h.ArrowSize = 8;
h.EdgeColor = 'k';

% ˢ��ͼ�δ���
drawnow;