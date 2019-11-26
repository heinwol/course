
clear all
syms x1 x2 x3 x4
syms lambda_c lambda_p K_c k_c k_p k_t  K_t k_r K_p lambda_r lambda_t P_0 C_0 mu_c mu_p gamma_p gamma_c 

f1 = (k_c + mu_c*x2) * x1^(3/4) * (1 - (x1/C_0)^(1/4)) - ...
        (lambda_c*x1 * x4)/(K_c + (1 - x3));
f2 = (k_p + (mu_p*x1)/(K_p + x1))*x2*(1 - x2/P_0) - lambda_p*x2;
f3 = k_r - (lambda_r + gamma_p*x2 + gamma_c*x1)*x3;
f4 = (k_t*x3)/(K_t + (1 - x3)) - lambda_t*x4;
F = [f1; f2; f3; f4];

assume(x1 >= 0); assume(x2 >= 0); assume(x3 >= 0); assume(x4 >= 0);
assume([lambda_c, lambda_p, lambda_r, lambda_t], 'positive')
assume([K_c, k_c, k_t, K_t, k_r, K_p, k_p], 'positive')
assume([P_0, C_0, mu_c, mu_p, gamma_c, gamma_p], 'positive')
assumeAlso(x3 <= 1)


%x1 = 0
assume(x1 == 0);
S = solve(F, [x1, x2, x3, x4], 'ReturnConditions', true);
% S1 = Solution(1, :); S2 = Solution(2, :);
% assume(x1, clear); assume(x1 >= 0);

% x2 = 0
% напрямую - не решает
% F_on_plane = subs(F, x2, 0);  
% assume(x2 == 0);
% [y1, y2, y3, y4] = solve(F, [x1, x2, x3, x4], 'Real', true);

% x3 = 0
% F_on_plane = subs(F, x3, 0);
% [y1, y2, y3, y4] = solve(F_on_plane, [x1, x2, x3, x4], 'Real', true);
% Solution = [y1 y2 y3 y4];


% S1 = S1.' - для трансп.




