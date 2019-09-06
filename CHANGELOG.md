# Change Log

## [v0.1.0](https://github.com/2ndWatch/cloudendure-python/tree/v0.1.0) (2019-09-06)

[Full Changelog](https://github.com/2ndWatch/cloudendure-python/compare/v0.1.0...HEAD)

**Implemented enhancements:**

- Adjust machine replication [\#75](https://github.com/2ndWatch/cloudendure-python/issues/75)
- CLI authentication [\#66](https://github.com/2ndWatch/cloudendure-python/issues/66)
- Simplify project method args and init flow [\#55](https://github.com/2ndWatch/cloudendure-python/issues/55)
- Configurable disk type for blueprints [\#46](https://github.com/2ndWatch/cloudendure-python/issues/46)
- Configurable PublicIPAction for blueprints [\#45](https://github.com/2ndWatch/cloudendure-python/issues/45)
- Handle MFA/SAML between AWS and CloudEndure [\#5](https://github.com/2ndWatch/cloudendure-python/issues/5)
- Add replication control for machines [\#76](https://github.com/2ndWatch/cloudendure-python/pull/76) ([mbeacom](https://github.com/mbeacom))
- Project provisioning [\#72](https://github.com/2ndWatch/cloudendure-python/pull/72) ([mbeacom](https://github.com/mbeacom))
- delete-image and terminate added [\#69](https://github.com/2ndWatch/cloudendure-python/pull/69) ([twarnock](https://github.com/twarnock))
- Add cli auth and adjust user api token handling [\#67](https://github.com/2ndWatch/cloudendure-python/pull/67) ([mbeacom](https://github.com/mbeacom))
- Adjust init flow and user feedback [\#56](https://github.com/2ndWatch/cloudendure-python/pull/56) ([mbeacom](https://github.com/mbeacom))
- made step more readable.  modified input/output to just use critical data [\#53](https://github.com/2ndWatch/cloudendure-python/pull/53) ([twarnock](https://github.com/twarnock))
- Fix \#45 \#46 - Update config and CE module to update public\_ip and dis… [\#47](https://github.com/2ndWatch/cloudendure-python/pull/47) ([mbeacom](https://github.com/mbeacom))
- Step functions refactor.  get-terraform can use tagging module [\#44](https://github.com/2ndWatch/cloudendure-python/pull/44) ([twarnock](https://github.com/twarnock))

**Fixed bugs:**

- CloudEndure token usage not working [\#63](https://github.com/2ndWatch/cloudendure-python/issues/63)
- Running gen-terraform against tagless AMIs results in error [\#51](https://github.com/2ndWatch/cloudendure-python/issues/51)
- Update CloudEndureConfig to use destination\_account vs accounts [\#49](https://github.com/2ndWatch/cloudendure-python/issues/49)
- Adjust CLI/config consolidation to avoid overwrites with empty values [\#68](https://github.com/2ndWatch/cloudendure-python/pull/68) ([mbeacom](https://github.com/mbeacom))
- Check for nonetype before iterating through image.tags [\#52](https://github.com/2ndWatch/cloudendure-python/pull/52) ([mbeacom](https://github.com/mbeacom))

**Closed issues:**

- CE worker lambda diagram [\#54](https://github.com/2ndWatch/cloudendure-python/issues/54)

**Merged pull requests:**

- Add Github action for pypi build/publishing [\#77](https://github.com/2ndWatch/cloudendure-python/pull/77) ([mbeacom](https://github.com/mbeacom))
- changes to support STS.   [\#70](https://github.com/2ndWatch/cloudendure-python/pull/70) ([twarnock](https://github.com/twarnock))
- Update pythonpackage.yml [\#62](https://github.com/2ndWatch/cloudendure-python/pull/62) ([mbeacom](https://github.com/mbeacom))
- Update gh pages workflow [\#61](https://github.com/2ndWatch/cloudendure-python/pull/61) ([mbeacom](https://github.com/mbeacom))
- Update repo from transfer and make minor adjustments [\#60](https://github.com/2ndWatch/cloudendure-python/pull/60) ([mbeacom](https://github.com/mbeacom))
- Optimize SVG for size [\#59](https://github.com/2ndWatch/cloudendure-python/pull/59) ([mbeacom](https://github.com/mbeacom))
- Added diagram [\#58](https://github.com/2ndWatch/cloudendure-python/pull/58) ([twarnock](https://github.com/twarnock))
- Create CODE\_OF\_CONDUCT.md [\#57](https://github.com/2ndWatch/cloudendure-python/pull/57) ([mbeacom](https://github.com/mbeacom))
- Update config for single destination account [\#50](https://github.com/2ndWatch/cloudendure-python/pull/50) ([mbeacom](https://github.com/mbeacom))
- moved to sharing to a single account [\#48](https://github.com/2ndWatch/cloudendure-python/pull/48) ([twarnock](https://github.com/twarnock))

## [v0.0.10](https://github.com/2ndWatch/cloudendure-python/tree/v0.0.10) (2019-08-23)
[Full Changelog](https://github.com/2ndWatch/cloudendure-python/compare/docker-base-layer...v0.0.10)

**Merged pull requests:**

- Cross region support for copy\_and\_split. gen\_terraform fixes [\#43](https://github.com/2ndWatch/cloudendure-python/pull/43) ([twarnock](https://github.com/twarnock))

## [docker-base-layer](https://github.com/2ndWatch/cloudendure-python/tree/docker-base-layer) (2019-08-23)
[Full Changelog](https://github.com/2ndWatch/cloudendure-python/compare/v0.0.9...docker-base-layer)

**Merged pull requests:**

- Remove launch types [\#42](https://github.com/2ndWatch/cloudendure-python/pull/42) ([mbeacom](https://github.com/mbeacom))

## [v0.0.9](https://github.com/2ndWatch/cloudendure-python/tree/v0.0.9) (2019-08-22)
[Full Changelog](https://github.com/2ndWatch/cloudendure-python/compare/v0.0.8...v0.0.9)

**Closed issues:**

- Deprecate launch\_type throughout project [\#41](https://github.com/2ndWatch/cloudendure-python/issues/41)

## [v0.0.8](https://github.com/2ndWatch/cloudendure-python/tree/v0.0.8) (2019-08-22)
[Full Changelog](https://github.com/2ndWatch/cloudendure-python/compare/v0.0.7...v0.0.8)

**Implemented enhancements:**

- Generate generic output infrastructure-as-code projects for migration waves [\#29](https://github.com/2ndWatch/cloudendure-python/issues/29)

**Merged pull requests:**

- Step function [\#40](https://github.com/2ndWatch/cloudendure-python/pull/40) ([twarnock](https://github.com/twarnock))
- tf generator first pass. various fixes [\#39](https://github.com/2ndWatch/cloudendure-python/pull/39) ([twarnock](https://github.com/twarnock))

## [v0.0.7](https://github.com/2ndWatch/cloudendure-python/tree/v0.0.7) (2019-08-13)
[Full Changelog](https://github.com/2ndWatch/cloudendure-python/compare/v0.0.6...v0.0.7)

**Implemented enhancements:**

- Migrate all config items to config module [\#28](https://github.com/2ndWatch/cloudendure-python/issues/28)
- Update replication settings to conform to desired KMS usage [\#24](https://github.com/2ndWatch/cloudendure-python/issues/24)
- Update main CLI handling to employ defined exceptions/feedback loops [\#6](https://github.com/2ndWatch/cloudendure-python/issues/6)
- Add typing throughout and import annotations from future [\#35](https://github.com/2ndWatch/cloudendure-python/pull/35) ([mbeacom](https://github.com/mbeacom))
- Update documentation with events entry and logos [\#34](https://github.com/2ndWatch/cloudendure-python/pull/34) ([mbeacom](https://github.com/mbeacom))
- Move all configs to use Config for env and yaml [\#33](https://github.com/2ndWatch/cloudendure-python/pull/33) ([mbeacom](https://github.com/mbeacom))
- Add base event handler and implementation on launch function [\#32](https://github.com/2ndWatch/cloudendure-python/pull/32) ([mbeacom](https://github.com/mbeacom))
- Change image name to avoid blowup [\#26](https://github.com/2ndWatch/cloudendure-python/pull/26) ([twarnock](https://github.com/twarnock))

**Fixed bugs:**

- Bug in update blueprint flow [\#10](https://github.com/2ndWatch/cloudendure-python/issues/10)
- Image creation failure [\#9](https://github.com/2ndWatch/cloudendure-python/issues/9)
- Share AMI should pull image id from env/config [\#8](https://github.com/2ndWatch/cloudendure-python/issues/8)
- Bug in last launch checks in main cli [\#7](https://github.com/2ndWatch/cloudendure-python/issues/7)

**Closed issues:**

- Remove 3.6 support and prepare 0.0.7 [\#37](https://github.com/2ndWatch/cloudendure-python/issues/37)
- Upgrade docker images to buster [\#36](https://github.com/2ndWatch/cloudendure-python/issues/36)
- Event handling - track wave status [\#31](https://github.com/2ndWatch/cloudendure-python/issues/31)

**Merged pull requests:**

- Upgrade docker images and drop py3.6 support [\#38](https://github.com/2ndWatch/cloudendure-python/pull/38) ([mbeacom](https://github.com/mbeacom))
- update-encryption-key added [\#25](https://github.com/2ndWatch/cloudendure-python/pull/25) ([twarnock](https://github.com/twarnock))
- made image names not 'test' [\#23](https://github.com/2ndWatch/cloudendure-python/pull/23) ([twarnock](https://github.com/twarnock))
- v0.0.6 [\#22](https://github.com/2ndWatch/cloudendure-python/pull/22) ([mbeacom](https://github.com/mbeacom))

## [v0.0.6](https://github.com/2ndWatch/cloudendure-python/tree/v0.0.6) (2019-08-06)
[Full Changelog](https://github.com/2ndWatch/cloudendure-python/compare/v0.0.5...v0.0.6)

**Implemented enhancements:**

- Add python-fire to package dependencies [\#13](https://github.com/2ndWatch/cloudendure-python/issues/13)
- copy\_image and split\_image support [\#20](https://github.com/2ndWatch/cloudendure-python/pull/20) ([twarnock](https://github.com/twarnock))
- Add black to makefile [\#18](https://github.com/2ndWatch/cloudendure-python/pull/18) ([mbeacom](https://github.com/mbeacom))
- Add typing throughout base project [\#17](https://github.com/2ndWatch/cloudendure-python/pull/17) ([mbeacom](https://github.com/mbeacom))
- Check uses replica now.  Launch looks up project\_id and stops on replica. [\#16](https://github.com/2ndWatch/cloudendure-python/pull/16) ([twarnock](https://github.com/twarnock))

**Merged pull requests:**

- Fixed update\_blueprint to actually work [\#21](https://github.com/2ndWatch/cloudendure-python/pull/21) ([twarnock](https://github.com/twarnock))
- Create and share image changes. [\#19](https://github.com/2ndWatch/cloudendure-python/pull/19) ([twarnock](https://github.com/twarnock))
- Update dependencies and adjust formatting [\#15](https://github.com/2ndWatch/cloudendure-python/pull/15) ([mbeacom](https://github.com/mbeacom))

## [v0.0.5](https://github.com/2ndWatch/cloudendure-python/tree/v0.0.5) (2019-06-28)
[Full Changelog](https://github.com/2ndWatch/cloudendure-python/compare/v0.0.4...v0.0.5)

**Implemented enhancements:**

- Add security policy [\#12](https://github.com/2ndWatch/cloudendure-python/issues/12)
- Add fire [\#14](https://github.com/2ndWatch/cloudendure-python/pull/14) ([mbeacom](https://github.com/mbeacom))

## [v0.0.4](https://github.com/2ndWatch/cloudendure-python/tree/v0.0.4) (2019-06-28)
[Full Changelog](https://github.com/2ndWatch/cloudendure-python/compare/v0.0.3...v0.0.4)

**Implemented enhancements:**

- Update docstrings, docs, and typing [\#11](https://github.com/2ndWatch/cloudendure-python/pull/11) ([mbeacom](https://github.com/mbeacom))

## [v0.0.3](https://github.com/2ndWatch/cloudendure-python/tree/v0.0.3) (2019-06-20)
[Full Changelog](https://github.com/2ndWatch/cloudendure-python/compare/v0.0.2...v0.0.3)

**Implemented enhancements:**

- Update pip dependencies [\#3](https://github.com/2ndWatch/cloudendure-python/pull/3) ([mbeacom](https://github.com/mbeacom))

**Merged pull requests:**

- Update README.md [\#4](https://github.com/2ndWatch/cloudendure-python/pull/4) ([twarnock](https://github.com/twarnock))

## [v0.0.2](https://github.com/2ndWatch/cloudendure-python/tree/v0.0.2) (2019-06-16)
[Full Changelog](https://github.com/2ndWatch/cloudendure-python/compare/v0.0.1...v0.0.2)

**Implemented enhancements:**

- Pointed API usecase and CLI additions [\#2](https://github.com/2ndWatch/cloudendure-python/pull/2) ([mbeacom](https://github.com/mbeacom))

## [v0.0.1](https://github.com/2ndWatch/cloudendure-python/tree/v0.0.1) (2019-05-30)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*