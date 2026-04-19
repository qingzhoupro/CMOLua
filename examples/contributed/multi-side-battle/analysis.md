# 三方对阵案例 - 代码解析

## 阵营态度代码

| 代码 | 态度 | 说明 |
|------|------|------|
| `"H"` | Hostile | 敌对 |
| `"F"` | Friendly | 友好 |
| `"N"` | Neutral | 中立 |
| `"U"` | Unfriendly | 不友好 |
| `"X"` | Unknown | 未知 |

## 感知级别（Awareness）

| 值 | 说明 |
|------|------|
| `"Blind"` | 盲目（完全无感知） |
| `"Normal"` | 正常感知 |
| `"AutoSideID"` | 自动识别阵营 |
| `"AutoSideAndUnitID"` | 自动识别阵营和单位 |
| `"Omniscient"` | 全知（观察者视角） |

## 熟练度（Proficiency）

| 值 | 说明 |
|------|------|
| `"Novice"` | 新手 |
| `"Cadet"` | 学员 |
| `"Regular"` | 普通 |
| `"Veteran"` | 老兵 |
| `"Ace"` | 王牌 |

## 关系设置要点

⚠️ **重要**：`ScenEdit_SetSidePosture()` 必须**双向设置**！

```lua
-- ⚠️ 阵营关系必须双向设置
ScenEdit_SetSidePosture("{{SIDE_A}}", "{{SIDE_B}}", "H")  -- A 对 B 敌对
ScenEdit_SetSidePosture("{{SIDE_B}}", "{{SIDE_A}}", "H")  -- B 对 A 敌对
```
