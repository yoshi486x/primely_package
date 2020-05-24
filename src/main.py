from primely.controller import controller


if __name__ == "__main__":
    # controller.paycheck_analysis()

    from primely.models import queueing, paycheck_analyzer

    """Queueing check"""
    # A = queueing.extract_filenames()
    # print(A)

    """Full analyze check"""
    full_analyzer = paycheck_analyzer.FullAnalyzer()

    # top 
    full_analyzer.starting_msg()
    full_analyzer.create_input_queue()
    
    # middle
    full_analyzer.process_all_input_data()
    full_analyzer.create_dataframe_in_time_series()
    paycheck_series = full_analyzer.get_packaged_paycheck_series()
    
    # bottom
    full_analyzer.export_in_jsonfile(paycheck_series)
    full_analyzer.export_income_timeline()
    full_analyzer.ending_msg()