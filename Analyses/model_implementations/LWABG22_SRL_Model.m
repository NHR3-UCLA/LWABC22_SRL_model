function [srl, srl_med, tau_srl] = LWABG22_SRL_Model(mag, wrup_max, F_D, eps)
% Lavrentiadis, Wang,  Abrahamson, Bozorgnia, and Goulet (2022)
% Surface Rupture Lenght model

%Model coefficinets
%--------------------
%width model
b_1=-1.1602; 
b_2= 0.0325;
%srl model
c_1   =-3.6913;
c_2   = 0.9205;
c_3   =-0.1567;
tau_u = 0.2568;

%Default inputs
%--------------------
if nargin<3; F_D=0; end
if nargin<4; eps=0; end

%Rupture Width Model
%--------------------
log_unb_wrup = b_1 + b_2*mag;
log_wrup     = min(log_unb_wrup, log10(wrup_max));

%Surface Rupture Length Model
%--------------------
%scaling term
x1 = mag - log_wrup;

%median surface rupture length
srl_med = 10.^( c_1 + c_2*x1 + c_3*F_D );

%aleatory std
tau_srl = tau_u / ( 1 + sigmoid_fun(2.1972*(log_unb_wrup-log10(wrup_max))/0.1) );

%surface rupture length
srl = srl_med .* 10.^(eps*tau_srl);

end

function y = sigmoid_fun(x)
%sigmoid_fun evaluates a simple sigmoid function along x: 

y = 1./(1 + exp(-x));

end
