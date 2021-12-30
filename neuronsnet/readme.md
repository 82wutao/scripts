模型 前馈 》结果 损失函数 》链式求导 后馈 》学习速率 * 导数 参数微调

```
input   lay     [X1,X2,X3,...,Xk]
hidden1 lay   [h1W1,h1W2,h1W3,...,h1Wk,h1a],active_func_h1;... m个节点 
hidden2 lay   [h2W1,h2W2,h2W3,...,h2Wm,h2a],active_func_h2;... n个节点
hidden3 lay   [h3W1,h3W2,h3W3,...,h3Wn,h3a],active_func_h3;... o个节点
...
out     lay   [oW1,oW2,oW3,...,oWo,oa],active_func_o
```

```
loss = loss_func([]expect,[]pred)
   sum((expect-pred)**2)
```

$$ Loss = L = (Yexpect - Ypred)^{2}$$

$$\frac{\partial L}{\partial ow1}$$
$$\frac{\partial L}{\partial Ypred} \ast \frac{\partial Ypred}{\partial ow1}$$
$$\frac{\partial (Yexpect - Ypred)^{2}}{\partial Ypred} \ast \frac{\partial active\_func\_o(h3N1*ow1+,...)}{\partial ow1}$$
$$ (-2 +2Ypred) \ast h3N1 * active\_func\_o'(h3N1*ow1+,...)$$

---
$$ h3N1 = ow1 * active\_func\_o'(h3N1*ow1+,...)$$
---


















