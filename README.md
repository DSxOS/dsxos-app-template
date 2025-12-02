# DSxOS Python Application Template
Description how to include the application in your site repository.

## Install into your site config repo
Choose one approach and adjust names/URLs as needed.

- Submodule:
  - `git submodule add <repo-url> external-modules/python/my-application`
  - `git submodule update --init --recursive`

- Subtree:
  - `git subtree add --prefix external-modules/python/my-application <repo-url> main --squash`

## Create app config
- Copy the sample and rename to match your app name:
  - `cp example_config.yaml config/external-modules/my-application.yaml`
- Edit the new file:
  - `appModule`: set a unique module name (e.g., `my-application`)
  - `containerName`: set a unique container name (e.g., `my-application`)
  - `cron`: set the schedule (e.g., `"0 * * * *"` for hourly)
  - `logLevel`: choose your level (e.g., `INFO`, `DEBUG`, `WARNING`)
  - `params`: add key-value pairs for any site-specific behavior (e.g., `apiEndpoint`, `environment`, feature flags). The application reads these via `raw_data["params"][<key>]`.

## Run behavior via params
- Pass all runtime customization through `params` in `config/external-modules/my-application.yaml`.
- Use the keys in code to control endpoints, toggles, credentials references, etc.
