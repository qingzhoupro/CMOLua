# 教训索引 | Lesson Index

> 教训库按根因分 3 大类。用户可在此文件追加新教训。
> Step 0.5 根据关键词匹配教训，不全量加载。

## 索引

| 教训 ID | 根因分类 | 触发关键词 | 所在文件 |
|---------|---------|-----------|---------|
| LOADOUTID | Lua 幻觉 | 飞机/Aircraft/F-16/歼击 | lesson-root-causes.md |
| GROUND-UNIT-TYPE | Lua 幻觉 | 地面/雷达/车辆/GROUND | lesson-root-causes.md |
| LATITUDE-PARAM | 地理坐标 | 经纬度/坐标/放置/latitude | lesson-root-causes.md |
| ALTITUDE-UNIT | 地理坐标 | altitude/高度/飞行高度 | lesson-root-causes.md |
| FACILITY-TERRAIN | 地理坐标 | 机场/跑道/Facility/水下 | lesson-root-causes.md |
| SIDE-NOT-EXIST | 意图理解 | 空白场景/添加单元/新建 | lesson-root-causes.md |
| SIDE-API | Lua 幻觉 | 创建阵营/AddSide | lesson-root-causes.md |
| DEPRECATED-DBID | Lua 幻觉 | 任何 DBID 引用/旧DBID | lesson-root-causes.md |
| MISSION-REF-POINT | 意图理解 | 巡逻/任务/参考点/patrol | lesson-root-causes.md |
| MISSION-TYPE-CASE | Lua 幻觉 | Attack/Strike/Patrol/攻击任务 | lesson-root-causes.md |
| MISSION-STRIKE-TYPE | Lua 幻觉 | strike/land/sea/空对地/火箭炮 | lesson-root-causes.md |
| DBID-TABLE-MATCH | Lua 幻觉 | DBID/GroundUnit/Facility/2434/3240 | lesson-root-causes.md |

## 用户添加教训格式

在 `lesson-root-causes.md` 对应分类下添加，格式：

```markdown
**教训-YOUR-ID** | 触发条件 | 错误信息 | 正确做法 | 自检项
```

然后在此索引追加一行。
