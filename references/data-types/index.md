# 数据类型参考索引

> AI 调用资料的索引 - 帮助 AI 找到正确的数据类型参考资料

## 快速导航

|| 数据类型 | 参考文档 |
|---------|----------|
|| 单位类型 | `overview.md` |
|| 高度/深度 | `altitude.md` |
|| 经纬度 | `latlon.md` |
|| 作战条令 | `doctrine.md` |

## 常用数据类型速查

### 单位类型 (type)

```lua
{type = "Aircraft"}  -- 飞机
{type = "Ship"}     -- 舰艇
{type = "Submarine"} -- 潜艇
{type = "Facility"} -- 设施/地面单位
```

### 感知级别 (Awareness)

```lua
{awareness = "Blind"}                   -- -1 盲目
{awareness = "Normal"}                   --  0  正常
{awareness = "AutoSideID"}              --  1  自动识别阵营
{awareness = "AutoSideAndUnitID"}        --  2  自动识别单位和阵营
{awareness = "Omniscient"}              --  3  全知
```

### 通讯中断 (outOfComms)

```lua
{outOfComms = "True"}   -- 网络中断，失去态势共享
{outOfComms = "False"}  -- 恢复正常通讯
```

```lua
{type = "Aircraft"}  -- 飞机
{type = "Ship"}     -- 舰艇
{type = "Submarine"} -- 潜艇
{type = "Facility"} -- 设施/地面单位
```

### 态度 (Stance)

```lua
ScenEdit_SetSidePosture(sideA, sideB, "H")  -- Hostile
ScenEdit_SetSidePosture(sideA, sideB, "F")  -- Friendly
ScenEdit_SetSidePosture(sideA, sideB, "N")  -- Neutral
ScenEdit_SetSidePosture(sideA, sideB, "U")  -- Unfriendly
```

### 熟练度 (Proficiency)

```lua
{proficiency = "Novice"}   -- 0
{proficiency = "Cadet"}    -- 1
{proficiency = "Regular"} -- 2
{proficiency = "Veteran"}  -- 3
{proficiency = "Ace"}      -- 4
```

### 任务类型 (MissionType)

```lua
{type = "Strike"}   -- 打击
{type = "Patrol"}    -- 巡逻
{type = "Mining"}    -- 布雷
{type = "Cargo"}     -- 运输
```

### 巡逻子类型 (PatrolSubtype)

```lua
{subtype = "ASW"}    -- 反潜
{subtype = "NAVAL"} -- 海上
{subtype = "AAW"}    -- 防空
{subtype = "LAND"}  -- 对地
```

### 高度格式

```lua
{altitude = "5000"}       -- 5000 米（默认）
{altitude = "5000 M"}     -- 5000 米
{altitude = "15000 FT"}   -- 15000 英尺
```

### 经纬度格式

```lua
{latitude = "35.0"}                    -- 数字格式
{latitude = "N 35.0"}                  -- 带方向
{latitude = "S 35.0"}
{longitude = "127.0"}                  -- 数字格式
{longitude = "E 127.0"}                -- 带方向
{longitude = "W 127.0"}
```

---

## AI 提示词模板

### 添加飞机
```
数据类型参考:
- altitude: "5000 M" 或 "15000 FT"
- latitude/longitude: 数字或 "N/E/S/W" 格式
- type: "Aircraft"
```

### 潜艇深度
```
数据类型参考:
- manualAltitude: 正数表示下潜深度
- 示例: {manualAltitude = 50} = 50米深度
```
