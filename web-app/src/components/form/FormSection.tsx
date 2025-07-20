import { useState } from 'react';
import { FormSectionProps } from '../../types';
import { cn } from '../../utils';

export const FormSection = ({ title, description, children, className }: FormSectionProps) => {
  const [isExpanded, setIsExpanded] = useState(true);

  return (
    <div className={cn('mb-6', className)}>
      <div
        className="flex items-center justify-between cursor-pointer mb-4 md:cursor-default"
        onClick={() => setIsExpanded(!isExpanded)}
      >
        <div>
          <h2 className="section-title text-lg md:text-xl">{title}</h2>
          {description && (
            <p className="text-gray-600 text-sm">{description}</p>
          )}
        </div>
        <button
          type="button"
          className="md:hidden text-gray-500 hover:text-gray-700"
          aria-label={isExpanded ? 'Collapse section' : 'Expand section'}
        >
          <svg
            className={cn('w-5 h-5 transition-transform', isExpanded && 'rotate-180')}
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M19 9l-7 7-7-7"
            />
          </svg>
        </button>
      </div>
      <div className={cn('space-y-4', !isExpanded && 'hidden md:block')}>
        {children}
      </div>
    </div>
  );
};
