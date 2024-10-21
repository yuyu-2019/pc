


%输入矩阵

% 创建图对象
G = digraph(A);

% 创建节点标签
nodeLabels = {'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', ...
              'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'Y'};

% 将节点标签分配给图对象
G.Nodes.Name = nodeLabels';


% 创建图形窗口

figure;

% 绘制有向图并设置布局为分层布局，不设置原始的节点标签
h = plot(G, 'Layout', 'layered', 'NodeLabel', {});

% 修改节点大小、颜色与形状
h.MarkerSize = 20;
h.NodeColor = 'r';
h.Marker = 'o';

% 修改特定节点的大小、颜色与形状
highlight(h, [2,6], 'NodeColor', [1 0.435 0.589], 'MarkerSize', 10, 'Marker', 'o');  % X1
highlight(h, [8], 'NodeColor', [1 0.588 0.443], 'MarkerSize', 10 , 'Marker', 'o');  % X1
highlight(h, [1,9,17], 'NodeColor', [1 0.780 0.3725], 'MarkerSize', 10, 'Marker', 'o'); % Y
highlight(h, [18,3,5], 'NodeColor', [1 0.435 0.589], 'MarkerSize', 10, 'Marker', 'o');  % X1
highlight(h, [13,4,15], 'NodeColor', [1 0.588 0.443], 'MarkerSize', 10 , 'Marker', 'o');  % X1
highlight(h, [7,12], 'NodeColor', [1 0.780 0.3725], 'MarkerSize', 10, 'Marker', 'o'); % Y
highlight(h, [19,11,10,14], 'NodeColor', [1 0.435 0.589], 'MarkerSize', 10, 'Marker', 'o');  % X1
highlight(h, [16], 'NodeColor', [1 0.588 0.443], 'MarkerSize', 10 , 'Marker', 'o');  % X1


highlight(h, [20], 'NodeColor', [0.3059 0.7098 0.9804], 'MarkerSize', 10, 'Marker', 'p'); % Y

% 获取节点坐标
xData = h.XData;
yData = h.YData;

% 手动添加节点标签，并覆盖原始的节点标签


% 设置边的属性
h.LineWidth = 1.5;
h.ArrowSize = 8;
h.EdgeColor = 'k';

% 刷新图形窗口
drawnow;
