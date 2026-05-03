class Transform:
    def clean_data(self, df):
        print("Cleaning data...")
        df = df.dropna()
        return df

    def feature_engineering(self, df):
        print("Creating features...")

        # Risk score
        if 'MemoryComplaints' in df.columns and 'BehavioralProblems' in df.columns and 'CholesterolHDL' in df.columns:
            df['RiskScore'] = 0.5 * df['MemoryComplaints'] + 0.3 * df['BehavioralProblems'] + 0.2 * df['CholesterolHDL']

        return df

    def run(self, df):
        df = self.clean_data(df)
        df = self.feature_engineering(df)
        return df