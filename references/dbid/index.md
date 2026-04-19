# 常见装备 DBID 参考表

> **⚠ 本表仅收录最常用装备的速查参考，不可替代 MCP 查询。**
> 大多数场景下，**必须先通过 MCP 查询真实 DBID**，本表仅用于记忆最常见的几个值。
>
> 查询方法：`query_dbid("英文关键词")` 或 `read_query("SELECT ...")`
>
> ⚠ **MCP 查询必须使用英文！** 数据库字段为英文，中文搜索无结果。

---

## 空军基地 / 地面设施（type="Facility"，不需要 LoadoutID）

| 装备                                         | DBID | 说明           |
| -------------------------------------------- | ---- | -------------- |
| Runway (3200m)                               | 35   | 通用跑道       |
| Runway (1400m)                               | 945  | 短跑道         |
| Runway Access Point (Medium Aircraft)        | 307  | 停机坪连接点   |
| Single-Unit Airfield (2x 3201-4000m Runways) | 430  | 双跑道空军基地 |
| Single-Unit Airfield (1x 4000m+ Runway)      | 1995 | 大型单跑道基地 |
| Single-Unit Airfield (Heliport)              | 1957 | 直升机停机坪   |

---

## 舰艇（type="Ship"，不需要 LoadoutID）

### 航母

| 装备                      | DBID     | 说明         |
| ------------------------- | -------- | ------------ |
| CVN 68 Nimitz             | 429      | 尼米兹级首舰 |
| CVN 70 Carl Vinson        | 246, 423 | 尼米兹级     |
| CVN 71 Theodore Roosevelt | 37, 381  | 尼米兹级     |
| CVN 73 George Washington  | 657, 658 | 尼米兹级     |
| CVN 76 Ronald Reagan      | 341      | 尼米兹级     |
| CVN 77 George Bush        | 505      | 尼米兹级末舰 |

### 美国驱逐舰 / 巡洋舰

| 装备                             | DBID               | 说明               |
| -------------------------------- | ------------------ | ------------------ |
| DDG 51 Arleigh Burke (Flight I)  | 112                | 伯克级驱逐舰       |
| DDG 51 Arleigh Burke (Flight I)  | 438, 561, 797, 798 | 伯克级驱逐舰       |
| DDG 72 Mahan (Flight II)         | 111                | 伯克 Flight II     |
| DDG 79 Oscar Austin (Flight IIA) | 294, 443           | 伯克 Flight IIA    |
| DDG 85 McCampbell (Flight IIA)   | 445                | 伯克 Flight IIA    |
| CG 47 Ticonderoga (Baseline 0)   | 42                 | 提康德罗加级巡洋舰 |
| CG 56 San Jacinto (Baseline 2)   | 40                 | 提康德罗加级       |

### 俄罗斯舰艇

| 装备                               | DBID           | 说明             |
| ---------------------------------- | -------------- | ---------------- |
| TAKR Admiral Kuznetsov (Pr.1143.5) | 147, 656, 2633 | 库兹涅佐夫号航母 |

### 护卫舰

| 装备                           | DBID               | 说明                 |
| ------------------------------ | ------------------ | -------------------- |
| FFG 36 Underwood (Perry Class) | 116, 457, 560, 563 | 佩里级护卫舰         |
| FFG 01 Adelaide (Perry Class)  | 540                | 澳大利亚佩里级       |
| 1101 Cheng Kung (Perry Class)  | 104, 649           | 台湾成功级（佩里改） |

---

## 飞机（type="Aircraft"，必须指定 LoadoutID）

### 战斗机

| 装备                 | DBID | LoadoutID       | 说明           |
| -------------------- | ---- | --------------- | -------------- |
| F-16A Falcon         | 158  | 33, 757, 1988   | F-16A（美国）  |
| F-16CM Blk 52 Falcon | 322  | 122, 2284, 3417 | F-16C（美国）  |
| F-35A Lightning II   | 278  | —              | 美国空军 F-35A |
| F-35B Lightning II   | 534  | —              | 短距起降型     |
| F-35C Lightning II   | 824  | —              | 舰载型         |
| F-22A Raptor         | 333  | —              | 美国隐身战斗机 |
| Su-27S Flanker B     | 134  | —              | 俄罗斯侧卫     |
| Su-35S Flanker M     | 2689 | —              | 俄罗斯侧卫     |
| F-15E Strike Eagle   | 2709 |                 | F-15E          |

### 无人机 / 攻击机

| 装备             | DBID | LoadoutID | 说明           |
| ---------------- | ---- | --------- | -------------- |
| MQ-9A Reaper UAV | 1719 | 2230      | 美国死神无人机 |

### 预警 / 加油 / 运输机

| 装备                 | DBID     | 说明       |
| -------------------- | -------- | ---------- |
| E-3C Sentry (AWACS)  | 209, 304 | 美国预警机 |
| KC-135R Stratotanker | 1692     | 美国加油机 |
| KC-135E Stratotanker | 159      | 美国加油机 |
| A-10A Thunderbolt II | 445, 717 | 美国攻击机 |

---

## 潜艇（type="Submarine"，不需要 LoadoutID）

| 装备                              | DBID           | 说明                 |
| --------------------------------- | -------------- | -------------------- |
| SSN 688 Los Angeles (Flight I)    | 22, 33, 71, 76 | 洛杉矶级攻击核潜艇   |
| SSN 719 Providence (Flight II)    | 24, 25, 109    | 洛杉矶 Flight II     |
| SSN 774 Virginia (Flight I)       | 40, 74, 561    | 弗吉尼亚级攻击核潜艇 |
| SSN 778 New Hampshire (Flight II) | 551, 562       | 弗吉尼亚 Flight II   |
| SSN 784 North Dakota (Flight III) | 552, 563       | 弗吉尼亚 Flight III  |

---

## 武器（武器 DBID 用于 Loadout 配置）

| 武器                          | DBID | 说明                   |
| ----------------------------- | ---- | ---------------------- |
| AIM-120D AMRAAM               | 51   | 中距空空导弹（最新型） |
| AIM-120C-7 AMRAAM             | 718  | 中距空空导弹           |
| AGM-65D Maverick              | 1876 | 空对地导弹（红外型）   |
| AGM-65F Maverick              | 1874 | 空对地导弹（海基型）   |
| Mine [Floating, Contact Fuze] | 634  | 通用漂雷               |
| Mine [Bottom, Magnetic Fuze]  | 632  | 底雷                   |
| Mine [Moored, Contact Fuze]   | 633  | 锚雷                   |

---

## 数据库查询方法

### 1. 查询装备 DBID（通过 MCP）

```python
# 使用英文关键词，通过 MCP query_dbid 查询
query_dbid("F-16C Fighting Falcon")
query_dbid("Arleigh Burke destroyer")
query_dbid("Virginia class submarine")
```

### 2. 查询 LoadoutID（通过 MCP read_query）

```sql
-- 先查 DBID，再查 LoadoutID：
SELECT ID FROM DataAircraftLoadouts WHERE ComponentID = 322;

-- 验证 DBID 存在：
SELECT ID, Name FROM DataAircraft WHERE Name LIKE '%F-16%';
SELECT ID, Name FROM DataShip WHERE Name LIKE '%Arleigh Burke%';
```

### 3. 查询所有表

```sql
-- 通过 MCP list_tables() 可列出所有表
-- 主要表：DataAircraft, DataShip, DataSubmarine, DataFacility, DataWeapon, DataAircraftLoadouts, DataLoadout
```

### 4. Facility（地面设施）不需要 LoadoutID

```lua
-- ✅ Facility 正确写法（不需要 LoadoutID）：
ScenEdit_AddUnit({
    side = "Blue",
    type = "Facility",
    dbid = 35,       -- Runway (3200m)
    name = "Main Runway",
    latitude = 35.6762,
    longitude = 139.6503
})

-- ❌ Aircraft 必须有 LoadoutID（必须先查）：
ScenEdit_AddUnit({
    side = "Blue",
    type = "Aircraft",
    dbid = 322,            -- F-16CM Blk 52（必须通过 MCP 查询）
    LoadoutID = 122,       -- 必须通过 DataAircraftLoadouts 查询
    name = "F-16 #1",
    latitude = 35.6762,
    longitude = 139.6503
})
```
