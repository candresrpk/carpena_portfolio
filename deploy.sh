#!/bin/bash

# CONFIGURA TUS DATOS
BRANCH="main"  # o master si usas otra rama

echo "🚀 Compilando Tailwind CSS..."
python manage.py tailwind build || { echo "❌ Error en tailwind build"; exit 1; }

echo "📦 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput || { echo "❌ Error en collectstatic"; exit 1; }

echo "📂 Agregando archivos al repositorio..."
git add .

echo "📝 Ingresa el mensaje del commit:"
read COMMIT_MESSAGE

git commit -m "$COMMIT_MESSAGE" || { echo "⚠️ Nada nuevo para commitear."; }

echo "🚀 Enviando cambios a GitHub (rama: $BRANCH)..."
git push origin $BRANCH || { echo "❌ Error al hacer push. Verifica tu conexión o credenciales."; exit 1; }

echo ""
echo "✅ Código enviado a GitHub correctamente."
echo ""
echo "📌 Entra a PythonAnywhere y ejecuta:"
echo "    cd tu-proyecto"
echo "    git pull origin $BRANCH"
echo "    source ~/myenv/bin/activate"
echo "    pip install -r requirements.txt"
echo "    python manage.py migrate"
echo "    python manage.py collectstatic --noinput"
echo ""
echo "🌐 Luego ve a la pestaña 'Web' y haz clic en 'Reload'."
echo "🎉 ¡Despliegue completado!"
