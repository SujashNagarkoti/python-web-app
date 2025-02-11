   �         @https://downloads.raspberrypi.org/os_list_imagingutility_v3.json�       ����      %�(T$p         
     O K           �      date   Thu, 06 Feb 2025 03:51:43 GMT   server   Apache   vary   
User-Agent   last-modified   Wed, 05 Feb 2025 15:30:46 GMT   etag   "a361-62d66cf352e4a"   accept-ranges   bytes   content-length   41825   content-type   application/json {
    "imager": {
        "latest_version": "1.8.5",
        "url": "https://www.raspberrypi.com/software/",
        "devices": [
            {
                "name": "No filtering",
                "tags": [],
                "description": "Show every possible image",
                "matching_type": "inclusive"
            },
            {
                "name": "Raspberry Pi 5",
                "tags": [
                    "pi5-64bit",
                    "pi5-32bit"
                ],
                "default": true,
                "icon": "https://downloads.raspberrypi.com/imager/icons/RPi_5.png",
                "description": "Raspberry Pi 5, 500, and Compute Module 5",
                "matching_type": "exclusive"
            },
            {
                "name": "Raspberry Pi 4",
                "tags": [
                    "pi4-64bit",
                    "pi4-32bit"
                ],
                "icon": "https://downloads.raspberrypi.com/imager/icons/RPi_4.png",
                "description": "Models B, 400, and Compute Modules 4, 4S",
                "matching_type": "inclusive"
            },
            {
                "name": "Raspberry Pi Zero 2 W",
                "tags": [
                    "pi3-64bit",
                    "pi3-32bit"
                ],
                "icon": "https://downloads.raspberrypi.com/imager/icons/RPi_Zero_2_W.png",
                "description": "The Raspberry Pi Zero 2 W",
                "matching_type": "inclusive"
            },
            {
                "name": "Raspberry Pi 3",
                "tags": [
                    "pi3-64bit",
                    "pi3-32bit"
                ],
                "icon": "https://downloads.raspberrypi.com/imager/icons/RPi_3.png",
                "description": "Models B, A+, B+, and Compute Module 3, 3+",
                "matching_type": "inclusive"
            },
            {
                "name": "Raspberry Pi 2",
                "tags": [
                    "pi2-32bit"
                ],
                "icon": "https://downloads.raspberrypi.com/imager/icons/RPi_2.png",
                "description": "Model B",
                "matching_type": "inclusive"
            },
            {
                "name": "Raspberry Pi Zero",
                "tags": [
                    "pi1-32bit"
                ],
                "icon": "https://downloads.raspberrypi.com/imager/icons/RPi_Zero.png",
                "description": "Models Zero, Zero W, Zero WH",
                "matching_type": "inclusive"
            },
            {
                "name": "Raspberry Pi 1",
                "tags": [
                    "pi1-32bit"
                ],
                "icon": "https://downloads.raspberrypi.com/imager/icons/RPi_1B+.png",
                "description": "Models A, B, A+, B+, and Compute Module 1",
                "matching_type": "inclusive"
            }
        ]
    },
    "os_list": [
        {
            "name": "Raspberry Pi OS (64-bit)",
            "description": "A port of Debian Bookworm with the Raspberry Pi Desktop (Recommended)",
            "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
            "url": "https://downloads.raspberrypi.com/raspios_arm64/images/raspios_arm64-2024-11-19/2024-11-19-raspios-bookworm-arm64.img.xz",
            "extract_size": 5989466112,
            "extract_sha256": "ab2a881114b917d699b1974a5d6f40e856899868baba807f05e3155dd885818a",
            "image_download_size": 1236435364,
            "release_date": "2024-11-19",
            "init_format": "systemd",
            "devices": [
                "pi5-64bit",
                "pi4-64bit",
                "pi3-64bit"
            ]
        },
        {
            "name": "Raspberry Pi OS (32-bit)",
            "description": "A port of Debian Bookworm with the Raspberry Pi Desktop",
            "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
            "url": "https://downloads.raspberrypi.com/raspios_armhf/images/raspios_armhf-2024-11-19/2024-11-19-raspios-bookworm-armhf.img.xz",
            "extract_size": 5289017344,
            "extract_sha256": "7e0c743eaba8ba3c86e028ff996984134f921dce86cb99b11f60a600dde81b53",
            "image_download_size": 1233753744,
            "release_date": "2024-11-19",
            "init_format": "systemd",
            "devices": [
                "pi5-32bit",
                "pi4-32bit",
                "pi3-32bit",
                "pi2-32bit",
                "pi1-32bit"
            ]
        },
        {
            "name": "Raspberry Pi OS (Legacy, 32-bit)",
            "description": "A port of Debian Bullseye with security updates and desktop environment",
            "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
            "url": "https://downloads.raspberrypi.com/raspios_oldstable_armhf/images/raspios_oldstable_armhf-2024-10-28/2024-10-22-raspios-bullseye-armhf.img.xz",
            "extract_size": 4303355904,
            "extract_sha256": "ce788d53d84ee15fdf760cafc3985521d9cb9ef0299e3e2a2988699fb388abcb",
            "image_download_size": 948776888,
            "release_date": "2024-10-22",
            "init_format": "systemd",
            "devices": [
                "pi4-32bit",
                "pi3-32bit",
                "pi2-32bit",
                "pi1-32bit"
            ]
        },
        {
            "name": "Raspberry Pi OS (other)",
            "description": "Other Raspberry Pi OS based images",
            "icon": "icons/cat_raspberry_pi_os.png",
            "subitems": [
                {
                    "name": "Raspberry Pi OS Lite (64-bit)",
                    "description": "A port of Debian Bookworm with no desktop environment (Compatible with Raspberry Pi 3/4/400/5)",
                    "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
                    "url": "https://downloads.raspberrypi.com/raspios_lite_arm64/images/raspios_lite_arm64-2024-11-19/2024-11-19-raspios-bookworm-arm64-lite.img.xz",
                    "extract_size": 2755657728,
                    "extract_sha256": "8605f56b7e725607e6bab0d0e5e52343fb5988c2172c98d034b3801efc0909a8",
                    "image_download_size": 459000608,
                    "release_date": "2024-11-19",
                    "init_format": "systemd",
                    "devices": [
                        "pi5-64bit",
                        "pi4-64bit",
                        "pi3-64bit"
                    ]
                },
                {
                    "name": "Raspberry Pi OS Full (64-bit)",
                    "description": "A port of Debian Bookworm with desktop environment and recommended applications",
                    "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
                    "url": "https://downloads.raspberrypi.com/raspios_full_arm64/images/raspios_full_arm64-2024-11-19/2024-11-19-raspios-bookworm-arm64-full.img.xz",
                    "extract_size": 15166603264,
                    "extract_sha256": "eac806440c72431aaf36eb83e916dea1021b0befa249196b682b305575add268",
                    "image_download_size": 3098494844,
                    "release_date": "2024-11-19",
                    "init_format": "systemd",
                    "devices": [
                        "pi5-64bit",
                        "pi4-64bit",
                        "pi3-64bit"
                    ]
                },
                {
                    "name": "Raspberry Pi OS Lite (32-bit)",
                    "description": "A port of Debian Bookworm with no desktop environment",
                    "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
                    "url": "https://downloads.raspberrypi.com/raspios_lite_armhf/images/raspios_lite_armhf-2024-11-19/2024-11-19-raspios-bookworm-armhf-lite.img.xz",
                    "extract_size": 2550136832,
                    "extract_sha256": "ef4de775bc91e814212b41b3aa14e87290aa5dd9ee4ce0e378a121824514c560",
                    "image_download_size": 532543404,
                    "release_date": "2024-11-19",
                    "init_format": "systemd",
                    "devices": [
                        "pi5-32bit",
                        "pi4-32bit",
                        "pi3-32bit",
                        "pi2-32bit",
                        "pi1-32bit"
                    ]
                },
                {
                    "name": "Raspberry Pi OS Full (32-bit)",
                    "description": "A port of Debian Bookworm with desktop environment and recommended applications",
                    "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
                    "url": "https://downloads.raspberrypi.com/raspios_full_armhf/images/raspios_full_armhf-2024-11-19/2024-11-19-raspios-bookworm-armhf-full.img.xz",
                    "extract_size": 12327059456,
                    "extract_sha256": "736ce0cc22d193bd893637ab62cd6148fc64de948972ebeeda7324bd10ab8a98",
                    "image_download_size": 2859320892,
                    "release_date": "2024-11-19",
                    "init_format": "systemd",
                    "devices": [
                        "pi5-32bit",
                        "pi4-32bit",
                        "pi3-32bit",
                        "pi2-32bit",
                        "pi1-32bit"
                    ]
                },
                {
                    "name": "Raspberry Pi OS (Legacy, 32-bit) Lite",
                    "description": "A port of Debian Bullseye with security updates and no desktop environment",
                    "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
                    "url": "https://downloads.raspberrypi.com/raspios_oldstable_lite_armhf/images/raspios_oldstable_lite_armhf-2024-10-28/2024-10-22-raspios-bullseye-armhf-lite.img.xz",
                    "extract_size": 1971322880,
                    "extract_sha256": "e111928796490da9f1ec9a59e8f53ccd87642d10cf5f3509ece3289486813eab",
                    "image_download_size": 384068048,
                    "release_date": "2024-10-22",
                    "init_format": "systemd",
                    "devices": [
                        "pi4-32bit",
                        "pi3-32bit",
                        "pi2-32bit",
                        "pi1-32bit"
                    ]
                },
                {
                    "name": "Raspberry Pi OS (Legacy, 32-bit) Full",
                    "description": "A port of Debian Bullseye with security updates, desktop environment and recommended applications",
                    "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
                    "url": "https://downloads.raspberrypi.com/raspios_oldstable_full_armhf/images/raspios_oldstable_full_armhf-2024-10-28/2024-10-22-raspios-bullseye-armhf-full.img.xz",
                    "extract_size": 10779361280,
                    "extract_sha256": "429e95c00be025f55e6f403a3a468e464715f9784264f2545e946eea0c042e59",
                    "image_download_size": 2614304092,
                    "release_date": "2024-10-22",
                    "init_format": "systemd",
                    "devices": [
                        "pi4-32bit",
                        "pi3-32bit",
                        "pi2-32bit",
                        "pi1-32bit"
                    ]
                },
                {
                    "name": "Raspberry Pi OS (Legacy, 64-bit)",
                    "description": "A port of Debian Bullseye with security updates and desktop environment",
                    "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
                    "url": "https://downloads.raspberrypi.com/raspios_oldstable_arm64/images/raspios_oldstable_arm64-2024-10-28/2024-10-22-raspios-bullseye-arm64.img.xz",
                    "extract_size": 4584374272,
                    "extract_sha256": "b374e111cf0816cd80e1a320d2b746a2a3bb5c023d4e483e8a991f3197c69873",
                    "image_download_size": 909827740,
                    "release_date": "2024-10-22",
                    "init_format": "systemd",
                    "devices": [
                        "pi4-64bit",
                        "pi3-64bit"
                    ]
                },
                {
                    "name": "Raspberry Pi OS (Legacy, 64-bit) Lite",
                    "description": "A port of Debian Bullseye with security updates and no desktop environment",
                    "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
                    "url": "https://downloads.raspberrypi.com/raspios_oldstable_lite_arm64/images/raspios_oldstable_lite_arm64-2024-10-28/2024-10-22-raspios-bullseye-arm64-lite.img.xz",
                    "extract_size": 2109734912,
                    "extract_sha256": "c3c108dbe0bf11b44016a883dc9c7aec4d178f10faf828f527979ad01a53a428",
                    "image_download_size": 327266544,
                    "release_date": "2024-10-22",
                    "init_format": "systemd",
                    "devices": [
                        "pi4-64bit",
                        "pi3-64bit"
                    ]
                },
                {
                    "name": "Raspberry Pi OS (Legacy, 64-bit) Full",
                    "description": "A port of Debian Bullseye with security updates, desktop environment and recommended applications",
                    "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
                    "url": "https://downloads.raspberrypi.com/raspios_oldstable_full_arm64/images/raspios_oldstable_full_arm64-2024-10-28/2024-10-22-raspios-bullseye-arm64-full.img.xz",
                    "extract_size": 11765022720,
                    "extract_sha256": "c7fa825cf797c96d4f506937df4034c9a5729a030e30539417e57c3ad2f5656e",
                    "image_download_size": 2564925448,
                    "release_date": "2024-10-22",
                    "init_format": "systemd",
                    "devices": [
                        "pi4-64bit",
                        "pi3-64bit"
                    ]
                }
            ]
        },
        {
            "name": "Other general-purpose OS",
            "description": "Other general-purpose operating systems",
            "icon": "icons/cat_other_general_purpose_operating_systems.png",
            "subitems": [
                {
                    "name": "Ubuntu",
                    "description": "Choose from Ubuntu Desktop, Server, and Core images",
                    "icon": "https://assets.ubuntu.com/v1/85a9de76-ubuntu-icon.svg",
                    "subitems_url": "https://changelogs.ubuntu.com/raspi/os_list_imagingutility_ubuntu.json",
                    "devices": [
                        "pi2-32bit",
                        "pi3-32bit",
                        "pi3-64bit",
                        "pi4-32bit",
                        "pi4-64bit",
                        "pi5-64bit"
                    ]
                },
                {
                    "name": "Apertis",
                    "description": "Debian-based distribution aimed at embedded systems",
                    "icon": "https://images.apertis.org/rpi/apertis-logo.png",
                    "subitems_url": "https://images.apertis.org/rpi/apertis-oslist.json",
                    "website": "https://www.apertis.org/"
                },
                {
                    "name": "RISC OS Pi",
                    "description": "A fast and easily customised operating system for ARM devices",
                    "icon": "https://packages.riscosopen.org/rpi_imager/RISC_OS.png",
                    "subitems_url": "https://packages.riscosopen.org/rpi_imager/os_list_imagingutility.json"
                },
                {
                    "name": "Ultramarine Linux",
                    "description": "Ultramarine Linux is a Fedora-based Linux distribution designed to stay out of your way and be easy to use. All editions come with several tweaks preapplied to make initial setup and daily usage seamless.",
                    "icon": "https://raw.githubusercontent.com/Ultramarine-Linux/logos/refs/heads/lapis/pixmaps/rpi-imager.svg",
                    "subitems_url": "https://raw.githubusercontent.com/Ultramarine-Linux/anywhere/main/raspberry-pi/imager.json",
                    "website": "https://ultramarine-linux.org"
                },
                {
                    "name": "Alpine Linux",
                    "description": "A security-oriented, lightweight Linux distribution based on musl libc and busybox",
                    "icon": "https://alpinelinux.org/alpinelinux-logo-icon.svg",
                    "subitems_url": "https://alpinelinux.org/rpi-imager.json",
                    "website": "https://alpinelinux.org"
                },
                {
                    "name": "Bass OS",
                    "description": "A new take on Android for the Raspberry Pi, bringing the dynamic nature of Bass OS/Bliss OS to the ARM platform using Bass Toolkit to compile one source with multiple variants",
                    "icon": "https://bliss-bass.blisscolabs.dev/assets/logos/Bliss-Bass_logo.png",
                    "subitems_url": "https://raw.githubusercontent.com/Bliss-Bass/bass-rpi/refs/heads/main/bass-arm-os-sublist.json",
                    "website": "https://bliss-bass.blisscolabs.dev/bassarm.html"
                }
            ]
        },
        {
            "name": "Media player OS",
            "description": "Media player operating systems",
            "icon": "icons/cat_media_players.png",
            "subitems": [
                {
                    "name": "LibreELEC",
                    "description": "A Kodi Entertainment Center distribution",
                    "icon": "https://releases.libreelec.tv/noobs/LibreELEC_RPi/LibreELEC_RPi.png",
                    "subitems_url": "https://releases.libreelec.tv/os_list_imagingutility_le.json"
                },
                {
                    "name": "OSMC",
                    "description": "A fast and feature filled open source media center",
                    "website": "https://osmc.tv",
                    "icon": "http://download.osmc.tv/installers/noobs/NOOBS-Logo-2.png",
                    "subitems_url": "http://download.osmc.tv/installers/rpidiskwriterimages.json"
                },
                {
                    "name": "Volumio",
                    "description": "The Audiophile Music Player and Streamer",
                    "website": "https://volumio.com",
                    "icon": "https://updates.volumio.org/rpi-imager/rpi-imager-volumio-icon.png",
                    "subitems_url": "https://updates.volumio.org/rpi-imager/rpi-imager.json"
                },
                {
                    "name": "moOde audio player",
                    "description": "Audiophile music streamer for the Raspberry Pi",
                    "website": "https://moodeaudio.org",
                    "icon": "https://moodeaudio.org/assets/img/logo/moode-logo-d.png",
                    "subitems_url": "https://moodeaudio.org/rpi-imager-subitems.json"
                },
                {
                    "name": "piCorePlayer",
                    "description": "A complete audio system for the Raspberry Pi",
                    "website": "https://picoreplayer.org",
                    "icon": "https://repo.picoreplayer.org/images/pCP.png",
                    "subitems_url": "https://repo.picoreplayer.org/rpi-imager.json"
                }
            ]
        },
        {
            "name": "Emulation and game OS",
            "description": "Emulators for running retro-computing platforms",
            "icon": "icons/cat_emulation_and_games.png",
            "random": true,
            "subitems": [
                {
                    "name": "RetroPie",
                    "description": "Turn your Raspberry Pi into a retro-gaming machine",
                    "icon": "https://retropie.org.uk/retropie-logo-40x40.png",
                    "subitems_url": "https://retropie.org.uk/os_list_imagingutility.json"
                },
                {
                    "name": "Recalbox",
                    "description": "The retro-gaming OS supporting 100+ gaming systems!",
                    "icon": "https://upgrade.recalbox.com/latest/rpi-imager/recalbox.png",
                    "website": "https://www.recalbox.com/",
                    "subitems_url": "https://upgrade.recalbox.com/latest/rpi-imager/os_list_imagingutility_recalbox.json"
                }
            ]
        },
        {
            "name": "Other specific-purpose OS",
            "description": "Home automation, 3D printing and specialised operating systems",
            "icon": "icons/cat_other_specific_purpose_operating_systems.png",
            "subitems": [
                {
                    "name": "3D printing",
                    "description": "3D printer operating systems",
                    "icon": "icons/cat_3d_printing.png",
                    "random": true,
                    "subitems": [
                        {
                            "name": "OctoPi",
                            "description": "A Raspberry Pi distribution for 3D printers. Ships OctoPrint out-of-the-box.",
                            "website": "https://octopi.octoprint.org",
                            "icon": "https://octopi.octoprint.org/rpi-imager.png",
                            "subitems_url": "https://octopi.octoprint.org/rpi-imager.json"
                        },
                        {
                            "name": "OctoKlipperPi",
                            "description": "Includes the OctoPrint host software for 3d printers and Klipper 3D printer firmware service",
                            "website": "https://github.com/guysoft/OctoKlipperPi",
                            "icon": "https://github.com/guysoft/OctoKlipperPi/raw/main/media/rpi-imager-OctoKlipperPi.png",
                            "subitems_url": "https://unofficialpi.org/rpi-imager/rpi-imager-octoklipperpi.json"
                        },
                        {
                            "name": "Mainsail OS",
                            "description": "Klipper Firmware & Moonraker API and Mainsail UI - ready to print!",
                            "website": "https://os.mainsail.xyz",
                            "icon": "https://os.mainsail.xyz/rpi-imager.png",
                            "subitems_url": "https://os.mainsail.xyz/rpi-imager.json"
                        },
                        {
                            "name": "SimplyPrint - 3D print anywhere, smarter",
                            "description": "Effortlessly manage 1, 2 or 100 3D printers from anywhere with the SimplyPrint ecosystem - free and easy to set up (SimplyPrint plugin on top of OctoPrint)",
                            "website": "https://simplyprint.io/?utm_source=pi-imager",
                            "icon": "http://cdn.simplyprint.io/i/static/rpi-imager/icon_gradient.png",
                            "subitems_url": "https://simplyprint.io/rpi-imager/rpi-imager-simplypi.json"
                        },
                        {
                            "name": "Repetier-Server",
                            "description": "Out-of-the-box multiple 3d printer management solution for Raspberry Pi.",
                            "website": "https://www.repetier-server.com/",
                            "icon": "https://download4.repetier.com/files/server/images/repetierserver40.png",
                            "subitems_url": "https://download4.repetier.com/files/server/images/Repetier-Server.json"
                        },
                        {
                            "name": "PrintWatch OS",
                            "description": "Monitor your 3D Printers using AI for free.",
                            "website": "https://printpal.io",
                            "icon": "https://github.com/printpal-io/printwatch-raspberrypi-image/blob/main/logo-40.png",
                            "subitems_url": "https://raw.githubusercontent.com/printpal-io/printwatch-raspberrypi-image/main/rpi_imager.json"
                        },
                        {
                            "name": "DuetPi",
                            "description": "Raspberry Pi OS with software for Duet3D controllers.",
                            "website": "https://www.duet3d.com",
                            "icon": "https://github.com/Duet3D/DuetPi/raw/rpi-imager/duet3d.png",
                            "subitems_url": "https://github.com/Duet3D/DuetPi/raw/rpi-imager/rpi-imager.json"
                        }
                    ]
                },
                {
                    "name": "Home assistants and home automation",
                    "description": "Home assistant and home automation operating systems",
                    "icon": "icons/cat_home_automation.png",
                    "random": true,
                    "subitems": [
                        {
                            "name": "Home Assistant",
                            "description": "Open source home automation that puts local control and privacy first.",
                            "icon": "https://version.home-assistant.io/brand/logo.png",
                            "subitems_url": "https://version.home-assistant.io/rpi-imager-haos.json",
                            "website": "https://www.home-assistant.io"
                        },
                        {
                            "name": "RaspberryMatic",
                            "description": "Lightweight Linux OS for running a HomeMatic/homematicIP IoT central.",
                            "icon": "https://raw.githubusercontent.com/jens-maus/RaspberryMatic/master/release/rpi-imager.png",
                            "subitems_url": "https://raw.githubusercontent.com/jens-maus/RaspberryMatic/master/release/rpi-imager.json",
                            "website": "https://raspberrymatic.de/"
                        },
                        {
                            "name": "nymea",
                            "description": "Smart Home/IoT platform, easy to use, open-source and privacy-focused.",
                            "icon": "https://raw.githubusercontent.com/nymea/nymea/master/icons/nymea-logo-48x48.png",
                            "subitems_url": "https://downloads.nymea.io/images/raspberrypi/rpi-image-repo.json",
                            "website": "https://nymea.io/users"
                        },
                        {
                            "name": "Gladys Assistant",
                            "description": "A privacy-first, open-source home assistant that runs on the Raspberry Pi.",
                            "icon": "https://gladysassistant.com/img/external/raspberry-pi-imager/icon-raspberry-pi-imager-40x40.png",
                            "subitems_url": "https://gladysassistant.com/img/external/raspberry-pi-imager/raspberry-pi-imager-gladys-assistant.json"
                        },
                        {
                            "name": "openHAB",
                            "description": "A vendor and technology agnostic open source automation software for your home.",
                            "icon": "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgMzIgMzIiPgoJPGNpcmNsZSBjeD0iMTYiIGN5PSIxNiIgcj0iMTYiIGZpbGw9IiNmZmYiLz4KCTxwYXRoIGZpbGw9IiNlNjRhMTkiIGQ9Im01LjI0MiAyMS4xMzMgOS4zOS05LjM5OEwxNiAxMC4zNjhsMS4zNjcgMS4zNjcgNi45MzMgNi45MzMtLjAxLjAzNS0uMTM3LjQwMi0uMTU2LjM5NC0uMTc0LjM4My0uMTkyLjM3NC0uMTc1LjMwNEwxNiAxMy4xMDMgNi4yNCAyMi44N2MtLjM3Ny0uNTUzLS43MjUtMS4xMjMtLjk5OC0xLjczOHoiLz4KCTxwYXRoIGZpbGw9IiM0NzQ3NDciIGQ9Ik0xNiA0YzYuNjEgMCAxMiA1LjM5IDEyIDEycy01LjM5IDEyLTEyIDEyYy0zLjYxIDAtNi44NTYtMS42MS05LjA1OS00LjE0N2wuNDI0LS40MjUuMzA4LS4zMDguMzA4LS4zMS4zMDktLjMwNy4wMTMtLjAxM0ExMC4wNTcgMTAuMDU3IDAgMCAwIDE2IDI2LjA3N2M1LjU1IDAgMTAuMDc4LTQuNTI2IDEwLjA3OC0xMC4wNzdTMjEuNTUgNS45MjIgMTYgNS45MjJDMTAuNDQ5IDUuOTIyIDUuOTIyIDEwLjQ1IDUuOTIyIDE2YzAgLjc0Ny4wODMgMS40NzYuMjM5IDIuMTc4bC0uNjY4LjY3LS44OTMuODkzQTExLjkyMiAxMS45MjIgMCAwIDEgNCAxNkM0IDkuMzkgOS4zOSA0IDE2IDR6Ii8+Cjwvc3ZnPgo=",
                            "subitems_url": "https://github.com/openhab/openhabian/releases/latest/download/rpi-imager-openhab.json",
                            "website": "https://www.openhab.org"
                        },
                        {
                            "name": "Homebridge",
                            "description": "Turn your Raspberry PI into a HomeKit smart home bridge.",
                            "website": "https://www.homebridge.io/",
                            "icon": "https://user-images.githubusercontent.com/3979615/116509191-3c35f880-a906-11eb-9a7f-7cad7c2aa641.png",
                            "subitems_url": "https://homebridge.io/rpi-image-repo.json"
                        }
                    ]
                },
                {
                    "name": "Kali Linux",
                    "description": "Kali Linux is an open-source, Debian-based Linux distribution geared towards various information security tasks, such as Penetration Testing, Security Research, Computer Forensics and Reverse Engineering.",
                    "website": "https://www.kali.org/",
                    "icon": "https://www.kali.org/images/kali-linux-logo.svg",
                    "subitems_url": "https://www.kali.org/rpi-imager.json"
                },
                {
                    "name": "FullPageOS",
                    "description": "Display a full page browser on boot in kiosk mode",
                    "icon": "https://github.com/guysoft/FullPageOS/raw/devel/media/rpi-imager-FullPageOS.png",
                    "subitems_url": "https://unofficialpi.org/rpi-imager/rpi-imager-fullpageos.json"
                },
                {
                    "name": "MoodleBox",
                    "description": "MoodleBox is an open source distribution combining a wireless access point with a full featured Moodle server.",
                    "website": "https://moodlebox.net",
                    "icon": "https://moodlebox.net/img/icon.png",
                    "subitems_url": "https://moodlebox.net/moodlebox-rpi-imager.json"
                },
                {
                    "name": "Falcon Player (FPP)",
                    "description": "Falcon Player (FPP) is an appliance used for managing and controlling animated light shows",
                    "icon": "https://raw.githubusercontent.com/FalconChristmas/fpp/master/rpi-imager/rpi-imager_fpp_logo.png",
                    "website": "https://www.falconplayer.com/",
                    "subitems_url": "https://raw.githubusercontent.com/FalconChristmas/fpp/master/rpi-imager/rpi-imager_falcon_player.json"
                },
                {
                    "name": "DAKboard",
                    "description": "DAKboard is a customizable display for photos, calendar, news, weather and so much more! DAKboard makes it easy to get organized so you won\u2019t miss a thing.",
                    "website": "https://dakboard.com",
                    "icon": "https://static.dakboard.com/assets/img/dakboard-logos/dakboard-logo-favicon-large.png",
                    "subitems_url": "https://dakboard.com/site/download/raspberrypi"
                },
                {
                    "name": "VEX Tournament Manager",
                    "description": "VEX Tournament Manager is a set of programs and displays for hosting and controlling VEX Robotics Competition events.",
                    "website": "https://vextm.dwabtech.com",
                    "icon": "https://vextm.dwabtech.com/rpi-imager/tm.svg",
                    "subitems_url": "https://vextm.dwabtech.com/rpi-imager/rpi-imager-tm.json"
                },
                {
                    "name": "Anthias",
                    "description": "The world's most popular open source digital signage solution. Turn any TV into a powerful digital sign.",
                    "website": "https://anthias.screenly.io/",
                    "icon": "https://raw.githubusercontent.com/Screenly/Anthias/master/static/img/square-dark.svg",
                    "subitems_url": "https://gist.githubusercontent.com/nicomiguelino/ad53e1f0203aff388b66505579ee6393/raw/e075b6c18a0e1b16da0f3b6526b048e0ec04b176/anthias-os-sublist-v0.19.4"
                },
                {
                    "name": "FreedomBox",
                    "description": "A home server for privacy and data ownership (a Debian project).",
                    "website": "https://freedombox.org/",
                    "icon": "https://ftp.freedombox.org/pub/freedombox/hardware/raspberry64/icon.png",
                    "subitems_url": "https://ftp.freedombox.org/pub/freedombox/hardware/raspberry64/rpi-imager.json"
                },
                {
                    "name": "LoLaOS",
                    "description": "Debian Based Remote Desktop OS for Gaming",
                    "website": "https://lola-pc.com/downloads/",
                    "icon": "https://app.lola-pc.com/downloads/tools/LoLaOS.png",
                    "subitems_url": "https://app.lola-pc.com/downloads/tools/lola-os-list.json"
                },
                {
                    "name": "Web3 Pi",
                    "description": "Web3 Pi is an open-source project that enables users to easily set up a Full Ethereum Node using Raspberry Pi, offering automated configuration and monitoring capabilities.",
                    "icon": "https://web3-pi.github.io/release-json/40x40.png",
                    "subitems_url": "https://web3-pi.github.io/release-json/os-sublist-web3pi.json",
                    "website": "https://www.web3pi.io/welcome-box"
                },
                {
                    "name": "SatNOGS",
                    "description": "Open-source global network of ground stations for receiving and sharing satellite data.",
                    "icon": "https://images.satnogs.org/satnogs-logo-40px.png",
                    "subitems_url": "https://images.satnogs.org/rpi-imager.json",
                    "website": "https://satnogs.org/"
                }
            ]
        },
        {
            "name": "Freemium and paid-for OS",
            "description": "Freemium and paid-for digital signage, 3d printing and thin client operating systems",
            "icon": "icons/cat_other_specific_purpose_operating_systems.png",
            "subitems": [
                {
                    "name": "Digital signage OS",
                    "description": "Digital signage operating systems",
                    "icon": "icons/cat_digital_signage.png",
                    "random": true,
                    "subitems": [
                        {
                            "name": "info-beamer digital signage",
                            "description": "Turn your Raspberry Pi into a professional digital signage display or video wall",
                            "icon": "https://cdn.infobeamer.com/repo.png",
                            "subitems_url": "https://cdn.infobeamer.com/repo.json",
                            "website": "https://info-beamer.com"
                        },
                        {
                            "name": "XOGO Digital Signage",
                            "description": "Transform Your RPi into a Digital Sign",
                            "icon": "https://xogoarchive.blob.core.windows.net/public/Logo40x40.png",
                            "subitems_url": "https://xogoarchive.blob.core.windows.net/public/rpi_subitems.json",
                            "website": "https://www.xogo.io/getting-started"
                        },
                        {
                            "name": "Yodeck Digital Signage",
                            "description": "The Digital Signage platform built for the Raspberry Pi. Free and unlimited for a single screen.",
                            "icon": "https://player-image.yodeck.com/imager.png",
                            "subitems_url": "https://player-image.yodeck.com/imager_repo.json",
                            "website": "https://www.yodeck.com"
                        },
                        {
                            "name": "1Play Digital Signage",
                            "description": "Player for 1Play Digital Signage service",
                            "icon": "https://media.1play.tv/wl/media.1play.tv/logo_vertical_login.png",
                            "subitems_url": "https://media.1play.tv/rpi-imager-repo.json",
                            "website": "https://1play.tv"
                        },
                        {
                            "name": "Screenly Digital Signage",
                            "description": "The digital signage platform focused on security, reliability, and flexibility.",
                            "icon": "https://disk-images.screenlyapp.com/Screenly-Icon.svg",
                            "subitems_url": "https://storage.googleapis.com/disk-images.screenlyapp.com/pi-imaging-utility.json",
                            "website": "https://screenly.io"
                        },
                        {
                            "name": "Linutop OS",
                            "description": "Digital Signage and Kiosk for the Raspberry Pi. Free Demo version",
                            "icon": "https://doc.linutop.com/raspi/imager.png",
                            "subitems_url": "https://doc.linutop.com/raspi/rpi-imager-repo.json",
                            "website": "https://www.linutop.com"
                        }
                    ]
                },
                {
                    "name": "3D printing",
                    "description": "3D printer operating systems",
                    "icon": "icons/cat_3d_printing.png",
                    "random": true,
                    "subitems": [
                        {
                            "name": "3DPrinterOS",
                            "description": "Allows you to manage your 3D printers fleet from anywhere",
                            "icon": "https://rpi-imager.3dprinteros.com/3dprinteros.png",
                            "subitems_url": "https://rpi-imager.3dprinteros.com/os-list-3dprinteros.json",
                            "website": "https://www.3dprinteros.com/"
                        }
                    ]
                },
                {
                    "name": "Android by emteria",
                    "description": "Android OS for your Raspberry Pi",
                    "icon": "https://emteria.com/hubfs/logos_emteria/rpi-imager.png",
                    "website": "https://emteria.com/lp/raspberry-pi-imager-android",
                    "subitems_url": "https://s3.emteria.com/public/rpi-imager/rpi-android.json"
                },
                {
                    "name": "TLXOS",
                    "description": "Debian-based thin client and digital signage OS",
                    "icon": "http://rpi.thinlinx.com/NOOBS/TLX_RPi/TLXOS.png",
                    "subitems_url": "http://rpi.thinlinx.com/rpi-imager/rpi-imager.json"
                }
            ]
        },
        {
            "name": "Misc utility images",
            "description": "Bootloader EEPROM configuration, etc.",
            "icon": "icons/cat_misc_utility_images.png",
            "devices": [
                "pi5-64bit",
                "pi4-32bit",
                "pi3-32bit",
                "pi2-32bit",
                "pi1-32bit"
            ],
            "subitems": [
                {
                    "name": "Bootloader (Pi 5 family)",
                    "description": "Restore the factory default settings and change boot priority",
                    "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
                    "subitems_url": "https://downloads.raspberrypi.com/eeprom_recovery_2712.json",
                    "devices": [
                        "pi5-64bit"
                    ]
                },
                {
                    "name": "Bootloader (Pi 4 family)",
                    "description": "Restore the factory default settings and change boot priority",
                    "icon": "https://downloads.raspberrypi.com/raspios_armhf/Raspberry_Pi_OS_(32-bit).png",
                    "subitems_url": "https://downloads.raspberrypi.com/eeprom_recovery.json",
                    "devices": [
                        "pi4-64bit",
                        "pi4-32bit"
                    ]
                },
                {
                    "name": "PINN",
                    "description": "A multi-boot OS installer with OS admin features",
                    "icon": "http://raw.githubusercontent.com/procount/pinn-os/master/os/pinn.png",
                    "subitems_url": "https://raw.githubusercontent.com/procount/pinn-os/master/iu/os_list_iu_pinn.json"
                }
            ]
        }
    ]
}
