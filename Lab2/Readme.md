# Computational-Mathematics
My Labs from Computational Mathematics. 4th semester. 


# Lab2 
Ответы на вопросы лабораторной работы. 

## 1. _Понятие точного и приближенного решений нелинейного уравнения._

Эти решения находят разными методами: 
  Точные -- позволяют найти решение непосредственно с помощью формул.
  итерационные -- приближенные, позволяют путем выполнения какой-то функции приближения получить ответ с заданной точностью.

## 2. _Основная идея метода половинного деления?_

Начальный интервал изоляции корня делим
пополам, получаем начальное приближение к корню: xo = (ao+bo)/2
И продолжим так делить до тех пор, пока |bn-an|>epsilon, конечно же, не забывая про теорему у существовании корня. (она поможет понять, какой границе интервала присвоить значение xi)



## 3. _Может ли метод половинного деления найти точное значение корня уравнения?_

Метод половинного деления обладает абсолютной сходимостью (близость получаемого
численного решения задачи к истинному решению.), просто он медленный (линейная сходимость), поэтому ждать долго. Кроме того, он будет определять лишь один из корней, если на интервале их несколько.

## 4. _В чем суть метода Ньютона?_

функция 𝑦 = 𝑓(𝑥) на отрезке [a, b] заменяется касательной и в качестве приближенного значения корня
𝑥∗ = 𝑥𝑛 принимается точка пересечения касательной с осью абсцисс.

xi = x_{i-1} - (f(x_{i-1}))/(f'(x_{i-1}))

## 5. _Как выбирается начальное приближение для метода Ньютона?_

Метод обеспечивает быструю сходимость, если выполняется условие:f(x0)**f''(x0)>0
и так для a и b. Но вообще достаточно и просто сходимости метода:
- y = f(x) определена и непрерывна на отрезке [𝑎; 𝑏] 
- f(a)·f(b) < 0 (на концах отрезка [a;b] функция имеет разные знаки)
- производные f'(x) и f''(x) сохраняют знак на отрезке [a;b]
- производная f'(x)≠0

## 6. _Идея метода хорд?_

функция 𝑦 = 𝑓(𝑥) на отрезке [a, b] заменяется хордой и в качестве
приближенного значения корня принимается точка пересечения хорды с осью абсцисс. 

xi = (ai*f(bi) - bi*f(ai))/(f(bi)-f(ai))

## 7. _Как выбирается начальное приближение для метода хорд с фиксированным концом интервала изоляции корня?_


1 случай.
x0 = a, граница b - зафиксирована
Производные имеют одинаковые знаки на отрезке [𝑎, 𝑏] :
𝒇′(𝒙) ∙𝒇′′(𝒙) >𝟎
𝑓′(𝑥)>0 и 𝑓′′(𝑥) > 0, функция возрастает и выпукла вниз
𝑓′(𝑥)<0 и 𝑓′′(𝑥) < 0, функция убывает и выпукла вверх

2 случай.
𝒙0 = b, граница a - зафиксирована
Производные имеют разные знаки на отрезке [𝑎, 𝑏] :
𝒇′(𝒙) ∙𝒇′′(𝒙) <𝟎
𝑓′(𝑥) < 0 и 𝑓′′(𝑥) > 0, функция убывает и выпукла вниз
𝑓′(𝑥) > 0 и 𝑓′′(𝑥) < 0, функция возрастает и выпукла вверх




## 8. _По каким причинам методы хорд и касательных предпочтительнее метода простой итерации?_

Недостатком метода простой итерации является его сходимость в малой окрестности корня и вытекающая отсюда необходимость выбора начального приближения к корню из этой малой окрестности. В противном случае итерационный процесс расходится или сходится к другому корню этого уравнения.


## 9. _Какой из методов является трехшаговым методом? Как запустить этот метод?_

???? пишите, если поняли суть вопроса...

## 10. _В чем суть метода простой итерации?_

Уравнение 𝑓 𝑥 = 0 приведем к эквивалентному виду: 𝑥 = 𝜑(𝑥), выразив 𝑥 из исходного уравнения.
Зная начальное приближение: 𝑥0 ∈ 𝑎, 𝑏 , найдем очередные приближения: 𝑥1 =𝜑(𝑥0)→𝑥2 =𝜑 𝑥1 ...

## 11. _Каковы условия применяемости метода простой итерации?_

выбора начального приближения к корню из малой окрестности для сходимости. 
Достаточное условие сходимости метода:
|𝜑′(𝑥)| ≤ 𝑞 < 1, где 𝑞 – некоторая константа (коэффициент Липшица или коэффициент
сжатия)
Чем меньше 𝑞, тем выше скорость сходимости.


## 12. _Как правильно преобразовать исходное нелинейное уравнение 𝑦 = 𝑓(𝑥) к виду 𝑥 = 𝜑(𝑥)?_
Есть несколько способов, но я советую третий: 
1. преобразуем уравнение 𝑓(𝑥) = 0 к равносильному (при 𝜆 ≠ 0) 𝜆𝑓(𝑥) = 0
2. прибавим 𝑥 в обеих частях: 𝑥=𝑥+𝜆𝑓(𝑥)
3. φ(𝑥) =𝑥 + 𝜆𝑓(𝑥), 𝜑′(𝑥) = 1 + 𝜆𝑓′(𝑥)
4. высокая скорость сходимости обеспечивается при 𝑞 = max 𝜑′(𝑥) ≈ 0  (max на [a,b])
5. Ну и не очень трудно выразить лямбда. - 1/(max(f'(x))) (max на [a,b])


## 13. _Каковы основные критерии окончания итерационного процесса?_

Процесс вычисления заканчивается при выполнении следующих условий:

Для уранений:
|𝑥_{𝑖+1}−𝑥𝑖| ≤𝜀, |𝑦_{𝑖+1}−𝑦𝑖| ≤𝜀

Для систем:
𝑚𝑎𝑥| 𝑥𝑖^(𝑘+1) − 𝑥𝑖^𝑘| ≤ 𝜀
## 14. _Как оценить необходимое количество итераций в методе биссекции при заданной точности?_ 

???????

## 15. _Алгоритм решения системы нелинейных уравнений методом Ньютона?_

https://algowiki-project.org/ru/Метод_Ньютона_для_систем_нелинейных_уравнений 
тут и схема есть, чтобы вам не страдать))

## 16. _Каковы преимущества и недостатки графического метода отделения решения для системы двух нелинейных уравнений?_
## 17. _В каких случаях можно применить метод простой итерации для решения системы нелинейных уравнений?_
## 18. _Когда можно считать итерационный процесс законченным при использовании метода простой итерации для решения системы нелинейных уравнений?_
## 19. _Что такое сходимость и скорость сходимости численных методов?_
## 20. _Дайте определение устойчивости итерационного метода?_










