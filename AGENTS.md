# AGENTS.md

This is a CopR packaging repo for [gpredict](https://github.com/csete/gpredict)
(C/GTK3 satellite-tracking app, autotools). The only artifact is `gpredict.spec` —
there is no application source, tests, CI, or build system in this repo.

## Spec conventions
- `Source0` is a URL to the upstream GitHub release tarball (no local tarball, no
  `sources` file). Do not add one unless switching to Fedora-official style.
- Upstream update: bump `Version`, reset `Release` to `1%{?dist}`, add `%changelog` entry.
  Re-release of same upstream: bump `Release` only, add `%changelog` entry.
- `%changelog` is Fedora format:
  `* <Day Mon DD YYYY> Jim Howard <xsnrg@users.noreply.github.com> - <version>-<release>`
  followed by `- ` bullets.
- Keep `%files` complete. Past mistakes: missing locale `.mo` files, the hicolor
  48x48 PNG icon, and the scalable SVG icon.
- Use only real RPM macros/tags: `GettextRequires` is not a real macro.
- `License` is `GPL-2.0-only` (upstream COPYING), not `-or-later`.

## Verification
- The real build is CopR: pushing to master triggers an automatic build.
- Locally, only on a Fedora/RHEL environment with RPM tooling:
  - `rpmlint gpredict.spec`
  - `rpmbuild -ba gpredict.spec` (put the upstream tarball in `~/rpmbuild/SOURCES`
    first, or use `rpmdev-rpmbuild` / `mock`).
- No test suite exists in this repo.

## Workflow
- Commit directly to master; commit style is lowercase, e.g. `fix spec: <description>`.
- Don't commit build artifacts, tarballs, or `.opencode/` tooling files.
