# ProFlowAI v2 Project Structure

```text
proflowai-v2/
  apps/
    api/
      app/
        api/
          v1/
            routes/
        core/
        db/
        models/
        repositories/
        schemas/
        services/
        utils/
        main.py
      alembic/
        versions/
      tests/
      requirements.txt
      Dockerfile
      alembic.ini
    web/
      src/
        app/
        components/
        features/
        layouts/
        pages/
        routes/
        services/
        types/
      public/
      package.json
      vite.config.ts
  packages/
    shared-types/
    ui/
  infrastructure/
    docker/
    scripts/
  docs/
```

This structure keeps deployment-facing applications under `apps/`, reusable packages under `packages/`, and environment or automation assets under `infrastructure/`.
