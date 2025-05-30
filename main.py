
import sys
from collector import DataCollector
from analyzer import FinancialAnalyzer


def main():
   
    instrument_id = "IE0002XZSHO1"  # votre ETF ISIN
    
    
    if len(sys.argv) > 1:
        instrument_id = sys.argv[1]
    
    print("="*80)
    print("Finacial performancee ")
    print("="*80)
    print(f"analyzing inis: {instrument_id}")
    print(f"Periods: YTD, 3M, 6M, 1Y, 3Y")
    
    
    collector = DataCollector()
    analyzer = FinancialAnalyzer()
    
    try:
        # Step 1: Data Collection
        print("\n" + "="*60)
        print("StEP 1: DATA COLLECTION")
        print("="*60)
        
        data = collector.collect_justetf_data(instrument_id)
        
        if not data:
            print(" Noo data collected....")
            return 1
        
        available_periods = collector.get_availaable_periods(data)
        print(f"\n Data collection is complete...: {', '.join(available_periods)}")
        
        # Step 2: Analysis
        print("\n" + "="*60)
        print("STEP 2: FInancial analysis")
        print("="*60)
        
        results = analyzer.analyze_all_periods(data)
        
        # Step 3: Results Display and Export
        print("\n" + "="*60)
        print("STEP 3: RESULTS")
        print("="*60)
        
        
        analyzer.export_results(results, 'console')
        
        
        analyzer.export_results(results, 'csv')
        analyzer.export_results(results, 'json')
        
        
        summary = analyzer.get_summary_stats(results)
        if 'message' not in summary:
            print(f"\n SUMMARY:")
            print(f"• Periods analyzed: {summary['periods_analyzed']}")
            print(f"• Best performance: {summary['best_performance']['period']} ({summary['best_performance']['value']:.2f}%)")
            print(f"• Highest volatility: {summary['highest_volatility']['period']} ({summary['highest_volatility']['value']:.2f}%)")
            print(f"• Maximum drawdown: {summary['max_drawdown']['period']} ({summary['max_drawdown']['value']:.2f}%)")
        
        print(f"\n Analysis completeE for instrument {instrument_id}")
        return 0
        
    except KeyboardInterrupt:
        print("\n Analysis issues")
        return 1
    except Exception as e:
        print(f"\n Errror annalysis: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)