# 活动图

## 开始/结束

```
start 
statement...
end
```

## 条件语句

```
start
if (condition A) then (yes)
  :Text 1;
elseif (condition B) then (yes)
  :Text 2;
  stop
elseif (condition C) then (yes)
  :Text 3;
elseif (condition D) then (yes)
  :Text 4;
else (nothing)
  :Text else;
endif
stop
```

## 循环

```
repeat循环
start
repeat
  :read data;
  :generate diagrams;
repeat while (more data?)
stop

while循环
start
while (data available?)
  :read data;
  :generate diagrams;
endwhile
stop
```

