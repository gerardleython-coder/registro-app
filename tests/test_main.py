from src.main import main

def test_main_runs(capfd):
    main()
    out, _ = capfd.readouterr()
    assert "Registro App iniciada." in out
