%MSEresults = table2array(MSEresults);
%MSEresults = table2array(MSEresults1);

plot(MSEresults(:, 1), MSEresults(:, 2), '-o', 'LineWidth', 10)

hold on;

plot(MSEresults(:, 1), MSEresults(:, 3), '-o', 'LineWidth', 10)

title("Average Draft Pick Distance by Draft Year");
xlabel("Draft Year");
ylabel("Average Draft Pick Distance");

legend("Actual Draft", "Mock Draft", "Location", 'southeast');

set(gca,'FontSize',30)
