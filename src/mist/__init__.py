# Disable GTK backend by default (causes issues on NixOS)
import matplotlib

matplotlib.use("Agg")
