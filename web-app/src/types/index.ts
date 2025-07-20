// Basic portrait information
export interface BasicInfo {
  purpose: string;
  attire: string;
  background: string;
  vibe: string;
}

// Advanced portrait settings
export interface AdvancedSettings {
  lighting: string;
  mood: string;
  age_range: string;
  gender: string;
  ethnicity: string;
  resolution: string;
}

// Additional profile information
export interface AdditionalInfo {
  reference_photo?: string | null;
  custom_notes?: string | null;
  preset_used?: string | null;
}

// Profile metadata
export interface Metadata {
  timestamp: string;
  version: string;
  created_by: string;
}

// Complete profile data structure
export interface ProfileData {
  basic_info: BasicInfo;
  advanced_settings: AdvancedSettings;
  additional_info: AdditionalInfo;
  metadata: Metadata;
  generated_prompt?: string | null;
}

// Form data interface for the UI
export interface FormData {
  // Basic Info
  purpose: string;
  attire: string;
  background: string;
  vibe: string;
  
  // Advanced Settings
  lighting: string;
  mood: string;
  age_range: string;
  gender: string;
  ethnicity: string;
  resolution: string;
  
  // Additional
  reference_photo?: File | null;
  custom_notes: string;
  save_profile: boolean;
  preset_name?: string;
}

// Preset data structure
export interface PresetData {
  name: string;
  purpose: string;
  attire: string;
  background: string;
  vibe: string;
  custom_notes: string;
  description?: string;
}

// Form validation result
export interface ValidationResult {
  isValid: boolean;
  message: string;
}

// API response interface
export interface ProfileResponse {
  profile: ProfileData;
  status: string;
  advanced_prompt: string;
  saved_file?: string;
}

// Dropdown option interface
export interface DropdownOption {
  value: string;
  label: string;
  icon?: string;
}

// Form section props
export interface FormSectionProps {
  title: string;
  description?: string;
  children: any; // Changed from React.ReactNode to any
  className?: string;
}
