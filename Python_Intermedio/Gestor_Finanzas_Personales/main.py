from interfaces import deploy_app
from logic import FinanceManager
from persistence import save_finance_info, export_csv, load_finance_info

def main():
    manager = FinanceManager()
    load_finance_info(manager)
    deploy_app(manager,
               fn_save=save_finance_info,
               fn_export=export_csv,)


if __name__ == '__main__':
    main()