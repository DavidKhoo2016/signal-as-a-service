from cockpit.dashboard import Dashboard
from fusion.fusion_core import FusionEngine

def test_fusion():
    engine = FusionEngine()
    engine.load_modules()
    for _ in range(10):
        engine.update_streams()
        signal = engine.get_fused_signal()
        print(f"[test] Fused Signal: {signal}")

def main():
    print("[main] Launching cockpit...")
    dashboard = Dashboard()
#    dashboard.run_live()
    try:
        dashboard.run_live()
    except Exception as e:
        print(f"\n[main] ❌ Cockpit crashed: {e}")
        input("[main] Press Enter to exit...")

if __name__ == "__main__":
    # Uncomment to test fusion manually
    # test_fusion()

    # Launch full cockpit
    main()
