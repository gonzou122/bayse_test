data{
  int N;
  vector[N] x;
  vector[N] y;
  int N_pred;
  vector[N_pred] x_pred;
}

parameters{
  real beta_0;
  real beta_1;
  real<lower=0> sigma;
}

model{
  for (i in 1:N){
    y[i] ~ normal(beta_0+beta_1*x[i],sigma);
  }
}

generated quantities{
  // 事後予測分布を得る
  vector[N_pred] mu_pred;
  vector[N_pred] y_pred;
  
  // Pythonと違って、添字は1から始まる
  for (i in 1:N_pred) {
    mu_pred[i] = beta_0+beta_1*x_pred[i];
    y_pred[i] = normal_rng(mu_pred[i], sigma);
  }

}