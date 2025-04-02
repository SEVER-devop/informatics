clc;
clear;

A = [3.6, 1.8, -4.7;
     2.7, -3.6, 1.9;
     1.5, 4.5, 3.3];
     
B = [3.8;
     0.4;
     -1.6];

det_A = det(A);

A1 = A;
A1(:,1) = B;
det_A1 = det(A1);

A2 = A;
A2(:,2) = B;
det_A2 = det(A2);

A3 = A;
A3(:,3) = B;
det_A3 = det(A3);

x1_kramer = det_A1 / det_A;
x2_kramer = det_A2 / det_A;
x3_kramer = det_A3 / det_A;
X_kramer = [x1_kramer; x2_kramer; x3_kramer];
disp('Method Kramera:');
disp(X_kramer);


A_inv = inv(A);
X_inv = A_inv * B;
disp('Obratnaya matrica:');
disp(X_inv);

