<div align="center">

```
    ____  ___   _____ ____     _________    _   ____ __
   / __ \/   | / ___// __ \   /_  __/   |  / | / / //_/
  / /_/ / /| | \__ \/ /_/ /    / / / /| | /  |/ / ,<
 / _, _/ ___ |___/ / ____/    / / / ___ |/ /|  / /| |
/_/ |_/_/  |_/____/_/        /_/ /_/  |_/_/ |_/_/ |_|

        R O B O T I C S   E X E R C I S E S
```

![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?logo=python&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-BCM%20GPIO-C51A4A?logo=raspberrypi&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%2F%20Raspberry%20Pi%20OS-333333)
![License](https://img.shields.io/badge/License-MIT-yellow)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

**基于树莓派 / Adeept RaspTank 的动手机器人课程 —— 从点亮 LED 到自主循线。**

**English · [简体中文](README.zh-CN.md)**

</div>

---

## 目录

- [项目简介](#项目简介)
- [机器人本体](#机器人本体)
- [课程模块](#课程模块)
- [硬件接线图](#硬件接线图)
- [环境配置](#环境配置)
- [运行练习](#运行练习)
- [项目演示](#项目演示)
- [项目成果](#项目成果)
- [安全须知](#安全须知)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

---

## 项目简介

一门循序渐进的动手机器人课程，围绕一台由树莓派驱动的 **Adeept RaspTank 履带式机器人** 展开。每个模块增加一项真实能力 —— 感知、执行或控制逻辑 —— 直到机器人能够自主沿标线赛道行驶。

设计目标：

- **难度递进** —— LED → 测距传感 → 电机控制 → 反应式避障 → 闭环循线
- **真实硬件、真实物理** —— 每个脚本都在实体机器人上运行，标定参数均有文档说明
- **代码易读、易于修改** —— 脚本刻意保持独立，便于单独学习、运行和改动

> 本项目旨在实践机器人学，深入理解传感器、控制逻辑与执行器如何在真实机器人中协同工作。

## 机器人本体

实际搭建 —— 树莓派大脑、超声波"眼睛"、底部的红外循线传感器、以及两条驱动履带：

<p align="center">
  <img src="assets/images/rasptank-photo.png" width="55%" alt="RaspTank 机器人" />
</p>

## 课程模块

| # | 模块 | 学习内容 | 脚本 |
|---|------|----------|------|
| 1 | **LED** | GPIO 输出、板载 LED、SPI 驱动 WS2812 RGB | `custom_led_pattern.py`、`ws2812_colors.py` |
| 2 | **超声波** | HC-SR04 测距、噪声滤波 | `ultrasonic_exercise.py`、`ultrasonic_filter.py` |
| 3 | **电机** | PWM 电机控制、标定直线行驶与转向 | `motor_speeds.py`、`move.py` |
| 4 | **避障** | 反应式控制回路、阈值整定 | `obstacle_alert.py`、`obstacle_avoidance.py` |
| 5 | **循线** | 红外传感器极性、差速控制、丢线恢复 | `line_sensor_raw.py`、`line_follow.py` |

## 硬件接线图

所有练习共用的接线与 GPIO 映射（BCM 编号）：

```
                    Raspberry Pi  ──  RaspTank
 ┌──────────────────────────────────────────────────────────────┐
 │                                                              │
 │  ULTRASONIC (HC-SR04)          MOTOR DRIVER (PCA9685 PWM)    │
 │  ├── TRIG ──► GPIO 23          ├── LEFT  track ── ch 2, 4    │
 │  └── ECHO ──► GPIO 24          └── RIGHT track ── ch 1, 3    │
 │                                                              │
 │  IR LINE SENSORS               LIGHTS                        │
 │  ├── LEFT   ◄── GPIO 22        ├── 3 onboard LEDs            │
 │  ├── MIDDLE ◄── GPIO 27        │     GPIO 9 / 25 / 11        │
 │  └── RIGHT  ◄── GPIO 17        └── 2 WS2812 RGB (spi_ws2812) │
 │                                                              │
 │  Robot library: /home/pi/raspTank/lib                        │
 └──────────────────────────────────────────────────────────────┘
```

> ⚠️ 运行脚本前请先核对你的机器人 —— 不同 RaspTank 版本的电机方向、传感器极性和接线可能不同。

## 环境配置

在树莓派上克隆仓库：

```bash
git clone https://github.com/nikgolobo/rasptank-robotics.git
cd rasptank-robotics
```

创建虚拟环境并安装依赖：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Adeept 专属的 `motor` 与 `spi_ws2812` 模块应已存在于机器人：

```text
/home/pi/raspTank/lib
```

## 运行练习

**1. LED**

```bash
python3 scripts/01_leds/custom_led_pattern.py
python3 scripts/01_leds/ws2812_colors.py
```

**2. 超声波传感器**

```bash
sudo python3 scripts/02_ultrasonic/ultrasonic_exercise.py
sudo python3 scripts/02_ultrasonic/ultrasonic_filter.py
```

**3. 电机控制**

```bash
sudo python3 scripts/03_motors/motor_speeds.py
sudo python3 scripts/03_motors/move.py
```

`move.py` 是带标定的正方形行驶版本，`TURN_TIME = 1.3`。

**4. 避障**

```bash
sudo python3 scripts/04_obstacle_avoidance/obstacle_alert.py
sudo python3 scripts/04_obstacle_avoidance/obstacle_avoidance.py
```

**5. 循线**

先查看红外传感器原始读数，再运行循线程序：

```bash
sudo python3 scripts/05_line_following/line_sensor_raw.py
sudo python3 scripts/05_line_following/line_follow.py
```

当前的 `line_follow.py` 是项目最新版本，采用 **差速履带速度** 实现更平滑的修正。

## 项目演示

两条真实室内标线赛道测试：

<p align="center">
  <a href="assets/videos/robot-course-test-01.mp4"><img src="assets/images/robot-course-test-01-preview.jpg" width="45%" alt="赛道测试 01 预览" /></a>
  <a href="assets/videos/robot-course-test-02.mp4"><img src="assets/images/robot-course-test-02-preview.jpg" width="45%" alt="赛道测试 02 预览" /></a>
</p>

| 测试 | 视频 |
|------|------|
| 赛道测试 01 | [▶ 观看 `robot-course-test-01.mp4`](assets/videos/robot-course-test-01.mp4) |
| 赛道测试 02 | [▶ 观看 `robot-course-test-02.mp4`](assets/videos/robot-course-test-02.mp4) |

这些视频记录了运动与导航行为的实车标定过程，说明物理机器人为何需要反复整定：转向与循迹性能取决于电机特性、电池电量、轮胎抓地力和地面材质。

详见 [`docs/media.md`](docs/media.md)。

## 项目成果

### 2026 年 Constructor University 夏令营

参加了 2026 年 **7 月 24 日至 8 月 4 日** 在德国不来梅举办的 **Constructor University 与 Constructor Talent School 夏令营**。

学术方向：

- 数学与建模
- 神经网络与机器人

夏令营内容包括机器人、传感器、编程与应用问题解决的动手实践。

## 安全须知

首次运行电机脚本时，请先将履带架空离开地面。确保机器人周围区域空旷，并随时准备用 `Ctrl+C` 停止程序。

## 贡献指南

欢迎提交贡献、问题和功能建议。请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)，并使用 [`.github/`](.github/) 中提供的 Issue/PR 模板。

## 许可证

本项目基于 [MIT 许可证](LICENSE) 发布。Copyright © 2026 Nikolay Goloborodko。

## 说明

本仓库有意将练习脚本保持为独立文件，而不封装成 Python 包 —— 因为它们直接控制硬件，设计初衷就是单独运行。

---

<div align="center">

**[⬆ 回到顶部](#rasptank-robotics)**

</div>
